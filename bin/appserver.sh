#!/bin/bash

python manage.py migrate --delete-ghost-migrations

python manage.py syncdb --noinput
python manage.py migrate --noinput
python manage.py runserver 0.0.0.0:8001
