import json

from kafka import KafkaConsumer
from clickhouse_driver import Client

from settings import settings


class KafkaConsumerManager:
    def __enter__(self):
        self.consumer = KafkaConsumer(
            'film_events',
            bootstrap_servers=settings.kafka_brokers.split(','),
            auto_offset_reset='earliest',
            enable_auto_commit=False,
            group_id='users-activities-messages',
            value_deserializer=lambda m: json.loads(m.decode('utf-8'))
        )
        return self.consumer

    def __exit__(self, exc_type, exc_value, traceback):
        self.consumer.close()


class ClickHouseClientManager:
    def __enter__(self):
        self.client = Client(host=settings.clickhouse_host)
        return self.client

    def __exit__(self, exc_type, exc_value, traceback):
        self.client.disconnect()
