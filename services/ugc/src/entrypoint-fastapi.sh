#!/usr/bin/env bash

python3 ./wait_for_kafka.py &
pid1=$!
wait $pid1

echo "Kafka is available. Starting UGC service..."

gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
