FROM python:3.7-alpine

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

RUN adduser -D -u 10001 noroot

USER noroot

CMD ["python", "python-kafka.py"]