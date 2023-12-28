from db.kafka import KafkaBroker


kafka: KafkaBroker | None = None


async def get_kafka() -> KafkaBroker:
    return kafka
