import json
from abc import ABC, abstractmethod
from kafka import KafkaProducer


class IBroker(ABC):
    @abstractmethod
    async def send(self, **kwargs):
        pass

    @abstractmethod
    async def close(self):
        pass


class KafkaBroker(IBroker):
    def __init__(self, **kwargs) -> None:
        self.connection = KafkaProducer(
            value_serializer=lambda v: json.dumps(v).encode('utf-8'),
            key_serializer=str.encode,
            **kwargs)

    def send(self, **kwargs):
        return self.connection.send(**kwargs)

    async def close(self):
        self.connection.close()
