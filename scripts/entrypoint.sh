#!/bin/sh

python manage.py migrate --no-input
python manage.py collectstatic --no-input

DJANGO_SUPERUSER_PASSWORD=$SUPER_USER_PASSWORD python manage.py createsuperuser --username $SUPER_USER_NAME --email $SUPER_USER_EMAIL --noinput

if [ $DEBUG = false ] ; then
    echo 'Running gunicorn...'
    gunicorn parking_control.wsgi:application --bind 0.0.0.0:8000
else
    echo 'Running manager.py runserver...'
    python manage.py runserver 0.0.0.0:8000
fi