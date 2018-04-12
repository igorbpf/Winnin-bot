web: gunicorn winnin_reddit.wsgi
worker: celery -A winnin_reddit worker -l info
beat: celery -A winnin_reddit beat -l info
