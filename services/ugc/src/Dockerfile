FROM python:3.11-alpine

WORKDIR /app


# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


COPY requirements.txt requirements.txt

# install dependencies
RUN apk update &&\
    apk add bash &&\
    apk add gcc && \
    apk add build-base libffi-dev openssl-dev python3-dev &&\
    apk add zlib-dev &&\
    pip install --no-cache-dir --upgrade pip &&\
    pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x ./entrypoint-fastapi.sh

ENTRYPOINT ["./entrypoint-fastapi.sh"]
