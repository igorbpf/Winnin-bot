import re
from rest_framework.generics import ListAPIView

from bot.serializers import PostSerializer, AuthorSerializer
from bot.models import Post


class PostView(ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        order = self.request.query_params.get('order')

        posts = Post.objects.all()

        if start_date and re.match(r'\d{4}-\d{1,2}-\d{1,2}',
                                   start_date, re.M | re.I):
            posts = posts.filter(created_at__gte=start_date)

        if end_date and re.match(r'\d{4}-\d{1,2}-\d{1,2}',
                                 end_date, re.M | re.I):
            posts = posts.filter(created_at__lte=end_date)

        if order:
            if order == 'ups' or order == 'num_comments':
                posts = posts.order_by('-' + order)

        return posts


class AuthorView(ListAPIView):
    serializer_class = AuthorSerializer

    def get_queryset(self):
        order = self.request.query_params.get('order')

        posts = Post.objects.all()

        if order:
            if order == 'ups' or order == 'num_comments':
                posts = posts.order_by('-' + order)

        return posts
