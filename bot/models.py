from django.db import models
from django.utils.translation import ugettext_lazy as _


class Post(models.Model):
    reddit_id = models.CharField(
        _('Reddit Id'),
        max_length=15
        )
    title = models.CharField(
        _('Title'),
        max_length=300,
        default='N/A'
        )
    author = models.CharField(
        _('Author'),
        max_length=60,
        default='N/A'
        )
    ups = models.IntegerField(
        _('Ups'),
        default=0
    )
    num_comments = models.IntegerField(
        _('Number of Comments'),
        default=0
    )
    created_at = models.DateTimeField(
        _('Created at'),
        )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('created_at',)
        verbose_name_plural = _('Posts')
