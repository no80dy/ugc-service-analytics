import json
import logging
from functools import lru_cache

from fastapi import Depends
from fastapi.encoders import jsonable_encoder

from db.broker import get_kafka
from db.kafka import KafkaBroker
from schemas.entity import UGCPayloads


class MessageService:
    """Класс MessageService содержит бизнес-логику по работе с сообщениями."""

    def __init__(
        self,
        broker: KafkaBroker
    ) -> None:
        self.broker = broker

    async def post_msg(self, topic: str, msg: UGCPayloads) -> bool:
        msg_payloads = jsonable_encoder(msg)
        key = str(msg_payloads.get('user_id'))
        try:
            self.broker.send(
                topic=topic,
                key=key,
                value=msg_payloads
            )
            return True
        except Exception as e:
            logging.info(e)
            return False


@lru_cache()
def get_message_service(
    kafka: KafkaBroker = Depends(get_kafka),
) -> MessageService:
    return MessageService(kafka)
