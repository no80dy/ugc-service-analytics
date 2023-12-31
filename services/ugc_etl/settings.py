import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    project_name: str = 'ugc'

    kafka_brokers: str = 'kafka-0:9092,kafka-1:9092,kafka-2:9092'
    default_topic: str = 'film_events'

    jwt_secret_key: str = 'secret'
    jwt_algorithm: str = 'HS256'

    batch_size: int = 50

    clickhouse_host: str = 'clickhouse-node1'
    clickhouse_port: int = 9000
    clickhouse_user: str = 'default'


settings = Settings()

# Корень проекта
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))