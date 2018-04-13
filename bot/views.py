from rest_framework.generics import ListAPIView

from bot.serializers import PostSerializer
from bot.models import Post


class PostView(ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
