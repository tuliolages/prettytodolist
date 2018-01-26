import factory
from django.test import TestCase

from todolists.models import TodoList, Task


class TodoListFactory(factory.DjangoModelFactory):
    class Meta:
        model = TodoList

class TaskFactory(factory.DjangoModelFactory):
    class Meta:
        model = Task
        django_get_or_create = ('todo_list',)


class TodoListsModelsTests(TestCase):
    def setUp(self):
        self.todo_list = TodoListFactory.create(name="my todo list")
        self.task = TaskFactory.create(
            todo_list=self.todo_list,
            description="my task description",
        )

    def test_todo_list_unicode(self):
        self.assertEqual(str(self.todo_list), "my todo list")

    def test_todo_list_attributes(self):
        self.assertEqual(self.todo_list.name, "my todo list")
        self.assertEqual(self.todo_list.tasks.count(), 1)

    def test_task_attributes(self):
        self.assertEqual(self.task.description, "my task description")
        self.assertIsNone(self.task.deadline)
        self.assertIsNone(self.task.completion_date)
        self.assertEqual(self.task.todo_list, self.todo_list)
        self.assertIsNone(self.task.assignee)