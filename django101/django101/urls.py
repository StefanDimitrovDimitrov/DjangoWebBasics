from django.contrib import admin
from django.urls import path, include




urlpatterns = [
    path('', include('django102.urls')),
    path('admin/', admin.site.urls),
    path('todos/', include('todos_app.urls')),
]
