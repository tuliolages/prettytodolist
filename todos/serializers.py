from rest_framework import serializers

from todos.models import TodoList, Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("id", "description", "deadline", "completion_date", "assignee",)

class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("id", "description", "todo_list",)


class TodoListSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True)

    class Meta:
        model = TodoList
        fields = ("id", "name", "tasks",)

class TodoListSimpleSerializer(serializers.ModelSerializer):
    pending_tasks_count = serializers.SerializerMethodField()

    def get_pending_tasks_count(self, obj):
        return obj.tasks.filter(completion_date__isnull=True).count()

    class Meta:
        model = TodoList
        fields = ("id", "name", "pending_tasks_count",)