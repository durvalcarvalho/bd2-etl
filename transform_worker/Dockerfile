FROM python:3.8-buster

ENV PYTHONUNBUFFERED 1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1

EXPOSE 8000

RUN mkdir /src

WORKDIR /src

COPY transform_worker/src /src

RUN pip3 install --upgrade pip==20.* && \
    pip3 install -r requirements.txt
