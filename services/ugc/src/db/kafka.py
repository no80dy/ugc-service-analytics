import json

from abc import ABC, abstractmethod
from aiokafka import AIOKafkaProducer


class IBroker(ABC):
    @abstractmethod
    async def send(self, **kwargs):
        pass

    @abstractmethod
    async def close(self):
        pass


class KafkaBroker(IBroker):
    def __init__(self, **kwargs) -> None:
        self.connection = AIOKafkaProducer(
            value_serializer=lambda v: json.dumps(v).encode('utf-8'),
            key_serializer=str.encode,
            **kwargs
        )

    async def send(self, **kwargs):
        return await self.connection.send(**kwargs)

    async def close(self):
        await self.connection.stop()
