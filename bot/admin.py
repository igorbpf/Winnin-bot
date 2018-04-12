from django.contrib import admin
from bot.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display_links = (
        'reddit_id',
        'title',
        'author',
        'ups',
        'num_comments',
        'created_at',
    )

    readonly_fields = (
        'reddit_id',
        'title',
        'author',
        'ups',
        'num_comments',
        'created_at',
    )

    list_display = (
        'reddit_id',
        'title',
        'author',
        'ups',
        'num_comments',
        'created_at',
    )
