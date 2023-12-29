import logging
import backoff
from time import sleep

from kafka import KafkaClient
from kafka.errors import NoBrokersAvailable, KafkaConnectionError

from core.config import settings

BACKOFF_MAX_TIME = 60

if __name__ == '__main__':

    @backoff.on_exception(
        backoff.expo,
        (KafkaConnectionError, NoBrokersAvailable),
        max_time=BACKOFF_MAX_TIME
    )
    def wait_for_kafka():
        try:
            kafka_client = KafkaClient(bootstrap_servers=f'{settings.kafka_brokers}')
            if kafka_client.bootstrap_connected():
                kafka_client.close()
                logging.info('Kafka is available')
                sleep(1)
            else:
                raise KafkaConnectionError
        except KafkaConnectionError:
            logging.info('Kafka is not available')
            raise KafkaConnectionError
        except NoBrokersAvailable:
            logging.info('Kafka is not available')
            raise NoBrokersAvailable

    wait_for_kafka()
