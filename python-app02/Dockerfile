FROM python:3.7-alpine

COPY . /src

RUN adduser -D -u 1001 noroot

USER noroot

CMD ["/bin/sh"]