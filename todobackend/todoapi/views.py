from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated  
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]  
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer