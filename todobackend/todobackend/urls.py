from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from todoapi import views
from rest_framework.authtoken.views import obtain_auth_token 
from todoapi import views

router = routers.DefaultRouter()
router.register(r'tasks', views.TaskViewSet)

urlpatterns = [
    path('', views.home),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  
]