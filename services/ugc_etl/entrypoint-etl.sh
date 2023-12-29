#!/usr/bin/env bash

python3 ./wait_for_kafka.py &
pid1=$!
wait $pid1

python3 ./wait_for_clickhouse.py &
pid1=$!
wait $pid1

python3 ./main.py
