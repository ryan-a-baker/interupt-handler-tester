FROM python:latest

WORKDIR /opt/interupt-handler

COPY ./ /opt/interupt-handler/

ENTRYPOINT ["python", "-u", "handler.py"]

