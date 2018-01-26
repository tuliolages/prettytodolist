from django.conf import settings
from django.db import models

from model_utils.models import TimeStampedModel


class TodoList(TimeStampedModel):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

class Task(TimeStampedModel):
    description = models.CharField(max_length=254)
    deadline = models.DateField(null=True, blank=True)
    completion_date = models.DateField(null=True, blank=True)
    todo_list = models.ForeignKey(TodoList, related_name="tasks")
    assignee = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, related_name="todo_lists")