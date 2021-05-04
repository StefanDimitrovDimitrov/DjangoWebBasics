
from django.contrib import admin
from django.urls import path

from django101.views import index, UserListView, GamesListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('2/', UserListView.as_view()),
    path('games/', GamesListView.as_view()),
]
