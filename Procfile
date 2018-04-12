web: gunicorn winnin_reddit.wsgi
worker: celery -A winnin_reddit worker -events -loglevel info
beat: celery -A winnin_reddit beat -l info
