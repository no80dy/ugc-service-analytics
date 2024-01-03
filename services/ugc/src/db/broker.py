from db.kafka import KafkaBroker


kafka: KafkaBroker | None = None


def get_kafka() -> KafkaBroker:
    return kafka
