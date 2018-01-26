from rest_framework import status
from rest_framework.test import APITestCase

from accounts.serializers import UserRegistrationSerializer, UserSerializer
from tests.python.accounts.test_models import UserFactory
from todolists.serializers import TodoListSerializer, TaskSerializer
from todolists.tests.test_models import TodoListFactory, TaskFactory
from todolists.models import TodoList, Task


class TodoListSerializerTest(APITestCase):
    def setUp(self):
        self.todo_list_attributes = {
            'name': 'my todo list'
        }

        self.valid_serializer_data = {
            'name': 'updated my todo list'
        }

        self.todo_list = TodoListFactory.create(**self.todo_list_attributes)
        self.serializer = TodoListSerializer(instance=self.todo_list)

    def test_todo_list_contains_expected_fields(self):
        data = self.serializer.data

        self.assertCountEqual(data.keys(), ['name', 'tasks'])

    def test_todo_list_fields_content(self):
        data = self.serializer.data

        self.assertEqual(data['name'], self.todo_list_attributes['name'])
        self.assertEqual(data['tasks'], [])
