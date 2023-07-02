#!/bin/sh

python manage.py migrate --database=store --noinput
python manage.py migrate --database=warehouse --noinput
python manage.py migrate --noinput

wait

python manage.py runserver 0.0.0.0:8000
