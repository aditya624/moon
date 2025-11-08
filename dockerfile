FROM python:3.11-slim

RUN apt-get update \
 && apt-get install -y --no-install-recommends ca-certificates openssl \
 && rm -rf /var/lib/apt/lists/*
 
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_NO_CACHE_DIR=on

WORKDIR /app

COPY . .

RUN python -m pip install --upgrade pip \
 && pip install --no-cache-dir .

# environment default
ENV APP_MODULE=moon.main:app \
    HOST=0.0.0.0 \
    PORT=8000

EXPOSE 8000

ENTRYPOINT ["/bin/sh", "-c", "uvicorn ${APP_MODULE} --host ${HOST} --port ${PORT:-8080}"]
