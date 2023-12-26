import os

from .logger import LOGGING
from pydantic_settings import BaseSettings
from logging import config as logging_config


class Settings(BaseSettings):
    project_name: str = 'ugc'

    jwt_secret_key: str = 'secret'
    jwt_algorithm: str = 'HS256'


settings = Settings()

# Применяем настройки логирования
logging_config.dictConfig(LOGGING)

# Корень проекта
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
