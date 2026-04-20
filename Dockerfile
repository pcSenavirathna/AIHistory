FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends ffmpeg \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.production.txt ./
RUN pip install --no-cache-dir -r requirements.production.txt

COPY main.py ./
COPY local_main.py ./
COPY app ./app
COPY data/grade10_dataset.csv ./data/grade10_dataset.csv
COPY data/grade11_dataset.csv ./data/grade11_dataset.csv

EXPOSE 8000

CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}"]
