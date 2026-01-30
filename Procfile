release: python manage.py collectstatic --noinput && python manage.py migrate
web: gunicorn URC.wsgi 
worker: python manage.py process_tasks --duration 0