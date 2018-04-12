import praw
from celery import shared_task
from decouple import config
from bot.models import Post
import datetime


def convert_unix2date(string):
    return datetime.datetime.fromtimestamp(
        int(string)
        ).strftime('%Y-%m-%d %H:%M:%S')


@shared_task
def get_posts():
    reddit = praw.Reddit(client_id=config('CLIENT_ID'),
                         client_secret=config('CLIENT_SECRET'),
                         username=config('USERNAME'),
                         password=config('PASSWORD'),
                         user_agent='winninbot')

    subreddit = reddit.subreddit('artificial')

    hot_artificial = subreddit.hot(limit=None)

    post_data = []

    for sub in hot_artificial:
        try:
            data = {
                'reddit_id': sub.id,
                'title': sub.title,
                'ups': int(sub.ups),
                'num_comments': int(sub.num_comments),
                'created_at': convert_unix2date(sub.created_utc),
                'author': sub.author.name
            }
            post_data.append(data)
        except AttributeError as e:
            print(e)
        except Exception as e:
            print(e)

    for post in post_data:
        Post.objects.update_or_create(
            reddit_id=post['reddit_id'],
            defaults=post
            )
