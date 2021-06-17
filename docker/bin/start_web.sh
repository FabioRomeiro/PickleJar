#!/bin/bash
uwsgi --ini /app/uwsgi.ini --processes=$UWSGI_PROCESSES

cd /app
./manage.py collectstatic --no-input
./manage.py migrate --no-input
tail -f /dkdata/uwsgi.log

cd /app/frontend/dist
http-server . -p 3000 --cors
