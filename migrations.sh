#!/bin/sh

python3 manage.py makemigrations
python3 manage.py makemigrations api

python3 manage.py migrate
python3 manage.py migrate api
