from django.urls import path, include
from rest_framework import routers
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls'))
]
