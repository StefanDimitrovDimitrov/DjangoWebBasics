from django.urls import path

from django102.views import index, UserListView, GamesListView, something

urlpatterns = [
    path('', index),
    path('2/', UserListView.as_view()),
    path('games/', GamesListView.as_view()),
    path('3/', something)
]
