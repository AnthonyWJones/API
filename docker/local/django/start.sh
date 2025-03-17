#!/bin/bash

set -o errexit

set -o pipefail

set -o nounset

python  manage.py migrate --no-input
python  manage.py collectstatic --no-input
exec python manage.py runserver 0.0.0.0:8000


#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

echo " Running Django Migrations..."
python manage.py migrate --no-input

echo " Collecting Static Files..."
python manage.py collectstatic --no-input

echo "Starting Django Development Server..."
exec python manage.py runserver 0.0.0.0:8000  #  Keeps the container running
