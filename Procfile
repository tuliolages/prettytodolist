web: gunicorn prettytodolist.wsgi --limit-request-line 8188 --log-file -
worker: celery worker --app=prettytodolist --loglevel=info
