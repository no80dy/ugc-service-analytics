import os

from pydantic_settings import BaseSettings
from logging import config as logging_config

from .logger import LOGGING


class Settings(BaseSettings):
    project_name: str = 'ugc'
    kafka_brokers: str = 'kafka-0:9092,kafka-1:9092,kafka-2:9092'
    default_topic: str = 'film_events'

    jwt_secret_key: str = 'secret'
    jwt_algorithm: str = 'HS256'


settings = Settings()

# Применяем настройки логирования
logging_config.dictConfig(LOGGING)

# Корень проекта
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
