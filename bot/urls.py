from django.urls import path
import bot.views as views

app_name = 'bot'

urlpatterns = [
    path('post/', views.PostView.as_view(),
         name='bot_post_list'),
]
