from django.urls import path

from django102.views import index, UserListView, GamesListView, something, methods_demo, create_game

urlpatterns = [
    path('', index),
    path('2/', UserListView.as_view()),
    path('games/', GamesListView.as_view()),
    path('3/', something),
    path('methods/', methods_demo),
    path('newgame/', create_game)
]
