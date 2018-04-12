import os
from celery import Celery
from django.conf import settings

# set the default Django settings module for the  'celery' program
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'winnin_reddit.settings')
app = Celery('winnin_reddit')

# Using a string here means the worker willnot have to pickle the object when
# using Windows
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
