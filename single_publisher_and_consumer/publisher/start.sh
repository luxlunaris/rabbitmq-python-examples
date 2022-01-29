#!/bin/bash
apt-get update && apt-get install -y netcat
while ! nc -z rabbitmq 5672; do sleep 3; done
python3 publisher.py