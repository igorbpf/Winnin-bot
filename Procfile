web: gunicorn winnin_reddit.wsgi
worker: celery -A winnin_reddit worker -l error
beat: celery -A winnin_reddit beat -l error
