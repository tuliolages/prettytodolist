from rest_framework import viewsets, generics

from todos.models import TodoList, Task
from todos.serializers import (
    TodoListSerializer,
    TodoListSimpleSerializer,
    TaskSerializer,
    TaskCreateSerializer
)


class TodoListSimpleListView(generics.ListCreateAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSimpleSerializer
    pagination_class = None

class TodoListViewSet(viewsets.ModelViewSet):
    serializer_class = TodoListSerializer
    queryset = TodoList.objects.all()

class TaskCreateView(generics.CreateAPIView):
    serializer_class = TaskCreateSerializer

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
