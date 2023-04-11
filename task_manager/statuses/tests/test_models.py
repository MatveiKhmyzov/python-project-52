from django.test import TestCase
from task_manager.statuses.models import Status


class TestStatusModel(TestCase):
    fixtures = ['statuses.json']

    @classmethod
    def setUpTestData(cls):
        cls.status = Status.objects.get(pk=2)

    def test_string_representation_of_status(self):
        expected_representation_status = 'on testing'
        self.assertEqual(expected_representation_status, str(self.status))
