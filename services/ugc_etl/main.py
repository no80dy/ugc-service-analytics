import json
import uuid

from kafka import KafkaConsumer
from clickhouse_driver import Client

from models import UserActivityModel
from settings import settings
from queries import insert_query
from logger import logger


def get_data_from_kafka():
	consumer = KafkaConsumer(
		'film_events',
		bootstrap_servers=['localhost:9094', ],
		auto_offset_reset='earliest',
		group_id='echo-messages-to-stdout',
		value_deserializer=lambda m: json.loads(m.decode('utf-8'))
	)
	client = Client(host='localhost')

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
						'event_time': user_activity_item.event_time.replace(microsecond=0)
					},
				)
				logger.info(f'Load to ClickHouse {user_activity_item}')
			user_activity_batch.clear()


if __name__ == '__main__':
	get_data_from_kafka()
