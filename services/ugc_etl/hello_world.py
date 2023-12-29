import time

from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9094', ])

producer.send(
	topic='messages',
	value=b'my message from python',
	key=b'python-message'
)

time.sleep(1)
