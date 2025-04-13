from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated  
from .models import Task
from .serializers import TaskSerializer
from django.http import JsonResponse

class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]  
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer


def home(request):
    return JsonResponse({
        "message": "🎉 Welcome to the Todo API!",
        "routes": {
            "Tasks endpoint": "/api/tasks/",
            "Token auth": "/api-token-auth/"
        }
    })