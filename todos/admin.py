from django.contrib import admin
from todos.models import TodoList, Task

admin.site.register(TodoList)
admin.site.register(Task)
