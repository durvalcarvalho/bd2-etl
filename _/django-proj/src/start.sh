#!/bin/bash

# Exporting all environment variables to use in crontab
env | sed 's/^\(.*\)$/ \1/g' > /root/env

# Função que espera o mysql ficar pronto antes de subir o server
function_mysql_ready() {
python << END
import socket
import time
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("db", 3306))
s.close()
END
}

echo '======= CHECKING FOR UNINSTALLED PKGs AND INSTALLING'
pip install -r requirements.txt

until function_mysql_ready; do
  >&2 echo "======= mysql IS UNAVAILABLE, WAITING"
  sleep 1
done
echo "======= mysql IS UP, CONNECTING"

echo '======= MAKING MIGRATIONS'
python3 manage.py makemigrations

echo '======= RUNNING MIGRATIONS'
python3 manage.py migrate

echo '======= RUNNING SERVER'
python3 manage.py runserver 0.0.0.0:8000