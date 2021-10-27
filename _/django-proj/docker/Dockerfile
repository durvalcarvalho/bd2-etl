FROM python:3.8-buster

ENV PYTHONUNBUFFERED 1

EXPOSE 8000

RUN mkdir /src

WORKDIR /src

COPY src /src

RUN pip3 install --upgrade pip==21.* && \
    pip3 install -r requirements.txt
