FROM python:3.12-slim

LABEL org.opencontainers.image.source=https://github.com/flexchar/tiktoken-counter/
LABEL org.opencontainers.image.description="API for counting tokens in a text using Tiktoken library."
LABEL org.opencontainers.image.licenses=MIT


WORKDIR /app

RUN pip install Flask tiktoken gunicorn

COPY . .

CMD ["gunicorn", "--preload", "--bind", "0.0.0.0:8000", "app:app"]
