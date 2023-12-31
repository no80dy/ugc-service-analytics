import sys
import backoff

from pathlib import Path
from time import sleep
from kafka import KafkaClient
from kafka.errors import NoBrokersAvailable, KafkaConnectionError

sys.path.append(str(Path(__file__).resolve().parents[1]))

from settings import settings
from logger import logger


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
                logger.info('Kafka is available')
                sleep(1)
            else:
                raise KafkaConnectionError
        except KafkaConnectionError:
            logger.info('Kafka is not available')
            raise KafkaConnectionError
        except NoBrokersAvailable:
            logger.info('Kafka is not available')
            raise NoBrokersAvailable

    wait_for_kafka()
