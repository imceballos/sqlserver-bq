FROM python:3.11.1-slim

COPY ./requirements.txt /src/requirements.txt
COPY ./start.sh /src/start.sh

RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt


CMD ["./src/start.sh"]

