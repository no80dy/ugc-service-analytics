import json
import uuid

from kafka import KafkaConsumer
from clickhouse_driver import Client


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
		data = message.value
		event_data_ = {'event_data': {}}
		event_data_json = json.dumps(
			event_data_
		)  # Преобразование в JSON-строку

		client.execute(
			f'INSERT INTO default.users_activity (id, user_id, film_id, event_name, event_data, event_time)'
			f'VALUES (generateUUIDv4(), generateUUIDv4(), generateUUIDv4(), \'{str(data["event_name"])}\', \'{event_data_json}\', today())'
		)


if __name__ == '__main__':
	get_data_from_kafka()
