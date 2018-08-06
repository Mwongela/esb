#!/bin/bash

NAME="es"
DIR=~/esb
USER=ubuntu
GROUP=ubuntu
WORKERS=3
BIND=unix:/home/ubuntu/esb/run/gunicorn.sock
DJANGO_SETTINGS_MODULE=es_backend.settings
DJANGO_WSGI_MODULE=es_backend.wsgi
LOG_LEVEL=error

cd $DIR
source venv/bin/activate

export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DIR:$PYTHONPATH

exec gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $WORKERS \
  --user=$USER \
  --group=$GROUP \
  --bind=$BIND \
  --log-level=$LOG_LEVEL \
  --log-file=-