#!/bin/bash

NAME="enem_importer"                           # Name of the application
DJANGODIR=/src                                 # Django project directory
PORT=${PORT:-8000}                               # we will communicte using this unix socket
USER=root                                      # the user to run as
GROUP=root                                     # the group to run as

NUM_WORKERS=${NUM_WORKERS:-16}                  # how many worker processes should Gunicorn spawn

WORKER_TIMEOUT=${WORKER_TIMEOUT:-60}           # Gunicorn worker timeout (in seconds)

NUM_THREADS=${NUM_THREADS:-4}                  # hoy many threads each worker can spawn to deal async requests

DJANGO_SETTINGS_MODULE=config.settings         # which settings file should Django use
DJANGO_WSGI_MODULE=config.wsgi                 # WSGI module name

LOG_FILE=/src/logs/gunicorn.log
ACCESS_LOG_FILE=/src/logs/nginx-access.log
RELOAD=${DEVELOPMENT_MODE:-false}
LOG_LEVEL=${LOG_LEVEL:-info}

echo "Starting $NAME as `whoami` in port $PORT"
date
echo "Gunicorn Workers: $NUM_WORKERS"
echo "Gunicorn Threads: $NUM_THREADS"
echo "Gunicorn Worker Timeout: $WORKER_TIMEOUT"
echo "Development Mode: $RELOAD"

export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH


pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic --noinput --clear

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec gunicorn ${DJANGO_WSGI_MODULE} \
  --reload \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user $USER --group $GROUP \
  --bind 0.0.0.0:$PORT \
  --log-level debug \
  --timeout $WORKER_TIMEOUT \
  --threads $NUM_THREADS \
  # `if [ $DEVELOPMENT_MODE == True ]; then echo "--access-logfile $ACCESS_LOG_FILE"; fi`
  # `if [ $DEVELOPMENT_MODE == True ]; then echo "--log-file $LOG_FILE"; fi`
  # `if [ $RELOAD == True ]; then echo "--reload"; fi`  # Optionally enable auto reload on source code changes
  # `if [ $DEVELOPMENT_MODE == True ]; then echo "--reload"; fi`  # Optionally enable auto reload on source code changes
