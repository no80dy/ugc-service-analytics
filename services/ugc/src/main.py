import logging
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from kafka.admin import KafkaAdminClient, NewTopic
from kafka.errors import TopicAlreadyExistsError

from api.v1 import events
from core.config import settings
from db import broker
from db.kafka import KafkaBroker


async def create_topic(topic_name: str):
    """Создание топика в кафке автоматически перед принятием запросов"""
    try:
        logging.info('Start creating topic')
        admin_client = KafkaAdminClient(
            bootstrap_servers=f'{settings.kafka_brokers}',
            client_id='admin_client'
        )
        topic_list = [NewTopic(name=topic_name, num_partitions=3, replication_factor=3)]
        admin_client.create_topics(new_topics=topic_list, validate_only=False)
        logging.info('Topic is created')
    except TopicAlreadyExistsError:
        pass
    except NotImplementedError as e:
        logging.error('Topic is not created', e)


@asynccontextmanager
async def lifespan(app: FastAPI):
    broker.kafka = KafkaBroker(
        bootstrap_servers=f'{settings.kafka_brokers}'
    )
    # Автоматически создать топик в кафке
    await create_topic(settings.default_topic)
    yield
    await broker.kafka.close()


app = FastAPI(
    description='Сервис сбора статистики',
    version='1.0.0',
    # Конфигурируем название проекта. Оно будет отображаться в документации
    title=settings.project_name,
    # Адрес документации в красивом интерфейсе
    docs_url='/ugc/api/openapi',
    # Адрес документации в формате OpenAPI
    openapi_url='/ugc/api/openapi.json',
    default_response_class=JSONResponse,
    lifespan=lifespan,
)


app.include_router(events.router, prefix='/ugc/api/v1/statistic', tags=['statistic'])


if __name__ == '__main__':
    # Приложение может запускаться командой
    # `uvicorn main:app --host 0.0.0.0 --port 8000 --reload`
    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=8000,
        reload=True
    )
