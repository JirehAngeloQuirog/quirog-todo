from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from todoapi import views

router = routers.DefaultRouter()
router.register(r'tasks', views.TaskViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]