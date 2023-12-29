FROM python:3.11-alpine

WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . .

RUN apk update &&\
    apk add bash &&\
    pip install --no-cache-dir --upgrade pip &&\
    pip install --no-cache-dir -r requirements.txt

RUN chmod +x ./entrypoint-etl.sh

ENTRYPOINT ["bash", "./entrypoint-etl.sh"]
