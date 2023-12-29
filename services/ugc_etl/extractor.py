import json

from kafka import KafkaConsumer


def get_data_from_kafka():
	consumer = KafkaConsumer(
		'messages',
		bootstrap_servers=['localhost:9094', ],
		auto_offset_reset='earliest',
		group_id='echo-messages-to-stdout',
		value_deserializer=lambda m: json.loads(m.decode('ascii'))
	)
