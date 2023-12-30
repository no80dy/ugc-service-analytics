import json
import backoff

from kafka import KafkaConsumer
from clickhouse_driver import Client
from kafka.errors import KafkaError
from clickhouse_driver.errors import Error as ClickHouseError

from models import UserActivityModel
from settings import settings
from queries import insert_query
from logger import logger


def connect_to_kafka() -> KafkaConsumer:
	try:
		consumer = KafkaConsumer(
			'film_events',
			bootstrap_servers=settings.kafka_brokers.split(','),
			auto_offset_reset='earliest',
			enable_auto_commit=True,
			group_id='users-activities-messages',
			value_deserializer=lambda m: json.loads(m.decode('utf-8'))
		)
		return consumer
	except KafkaError as err:
		logger.info(f'Error connecting to Kafka: {err}')


def connect_to_clickhouse():
	try:
		return Client(host='clickhouse-node1')
	except ClickHouseError as err:
		logger.info(f'Error connecting to ClickHouse: {err}')


def get_data_from_kafka():
	consumer = connect_to_kafka()
	client = connect_to_clickhouse()

	user_activity_batch = []
	for message in consumer:
		user_activity = UserActivityModel(**message.value)
		user_activity_batch.append(user_activity)

		logger.info(f'Add in batch {user_activity}')

		if len(user_activity_batch) >= settings.batch_size:
			for user_activity_item in user_activity_batch:
				client.execute(
					insert_query,
					{
						'id': str(user_activity_item.id),
						'user_id': str(user_activity_item.user_id),
						'film_id': str(user_activity_item.film_id),
						'event_name': user_activity_item.event_name,
						'comment': user_activity_item.comment,
						'film_sec': user_activity_item.film_sec,
						'like': user_activity_item.like,
						'event_time': user_activity_item.event_time.replace(microsecond=0)
					},
				)
				logger.info(f'Load to ClickHouse {user_activity_item}')
			user_activity_batch.clear()


if __name__ == '__main__':
	get_data_from_kafka()
