FROM python:3.10

WORKDIR /app
COPY requirements.txt ./

RUN apt update -y
RUN pip install -r requirements.txt

COPY . .
