FROM ubuntu:20.04

RUN apt-get update && apt-get install -y \
    software-properties-common \
    python3.8

RUN apt-get install -y python3-venv \
    python3-pip

RUN pip install mysql-connector-python
RUN pip install python-decouple
RUN pip install python-dotenv

RUN mkdir /app
WORKDIR /app

COPY src .

CMD [ "/app/run.sh" ]