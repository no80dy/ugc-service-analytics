import logging
from functools import lru_cache

from fastapi import Depends
from fastapi.encoders import jsonable_encoder
from kafka.errors import KafkaTimeoutError

from core.config import settings
from db.broker import get_kafka
from db.kafka import KafkaBroker
from schemas.entity import UGCPayloads


class EventService:
    """Класс EventService содержит бизнес-логику по работе с событиями."""

    def __init__(
        self,
        broker: KafkaBroker
    ) -> None:
        self.broker = broker

    async def post_event(
            self,
            event_payloads: UGCPayloads,
            topic: str = settings.default_topic
    ) -> bool:
        value = jsonable_encoder(event_payloads)
        key = str(value.get('user_id'))
        await self.broker.connection.start()
        try:
            await self.broker.send(
                topic=topic,
                key=key,
                value=value
            )
            return True
        except KafkaTimeoutError as e:
            logging.info(e)
            return False


@lru_cache()
def get_event_service(
    kafka: KafkaBroker = Depends(get_kafka),
) -> EventService:
    return EventService(kafka)
