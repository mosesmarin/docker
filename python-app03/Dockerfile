FROM python:3.7-alpine

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

RUN adduser -D -u 10001 10001

USER 10001

CMD ["python", "python-kafka.py"]