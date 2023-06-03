#!/bin/sh

python3 manage.py makemigrations
python3 manage.py makemigrations api

python3 manage.py migrate
python3 manage.py migrate api


echo "-----------Run server--------- "
python manage.py runserver 0.0.0.0:8000