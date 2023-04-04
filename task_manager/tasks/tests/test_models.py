from django.test import TestCase
from task_manager.tasks.models import Task


class TestCustomUserModel(TestCase):
    fixtures = ['users.json', 'statuses.json', 'tasks.json']

    @classmethod
    def setUpTestData(cls):
        cls.task = Task.objects.get(pk=1)

    def test_string_representation_of_task(self):
        expected_represenatation_customuser = 'read book'
        self.assertEqual(expected_represenatation_customuser, str(self.task))
