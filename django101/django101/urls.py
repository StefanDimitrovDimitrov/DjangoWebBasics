from django.urls import path, include

import django102
from django102.views import index, UserListView, GamesListView

urlpatterns = [
    path('', include('django102.urls'))
]
