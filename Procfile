release: python manage.py migrate

web: gunicorn pedalcity.wsgi --log-file - --log-level debug