from django.test import TestCase
from task_manager.tasks.models import Task


class TestTaskModel(TestCase):
    fixtures = ['users.json', 'statuses.json', 'tasks.json', 'labels.json']

    @classmethod
    def setUpTestData(cls):
        cls.task = Task.objects.get(pk=1)

    def test_string_representation_of_task(self):
        expected_representation_task = 'read book'
        self.assertEqual(expected_representation_task, str(self.task))
