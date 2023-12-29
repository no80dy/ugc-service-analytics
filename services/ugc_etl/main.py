import json
import uuid

from kafka import KafkaConsumer
from clickhouse_driver import Client

from models import UserActivityModel
from queries import insert_query


def get_data_from_kafka():
	consumer = KafkaConsumer(
		'film_events',
		bootstrap_servers=['localhost:9094', ],
		auto_offset_reset='earliest',
		group_id='echo-messages-to-stdout',
		value_deserializer=lambda m: json.loads(m.decode('utf-8'))
	)
	client = Client(host='localhost')

	for message in consumer:
		print(message.value)
		user_activity = UserActivityModel(**message.value)
		print(user_activity)
		# query = client.substitute_params(
		# 	insert_query,
		# 	{
		# 		'id': str(uuid.uuid4()),
		# 		'user_id': str(user_activity.user_id),
		# 		'film_id': str(user_activity.film_id),
		# 		'event_name': user_activity.event_name,
		# 		'comment': user_activity.comment,
		# 		'film_sec': user_activity.film_sec,
		# 		'event_time': user_activity.event_time.replace(microsecond=0)
		# 	},
		# 	client.connection.context
		# )
		# print(query)
		client.execute(
			insert_query,
			{
				'id': str(uuid.uuid4()),
				'user_id': str(user_activity.user_id),
				'film_id': str(user_activity.film_id),
				'event_name': user_activity.event_name,
				'comment': user_activity.comment,
				'film_sec': user_activity.film_sec,
				'event_time': user_activity.event_time.replace(microsecond=0)
			},
		)


if __name__ == '__main__':
	get_data_from_kafka()
