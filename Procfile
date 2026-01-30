release: python manage.py collectstatic --noinput
web: gunicorn URC.wsgi 
worker: python manage.py process_tasks