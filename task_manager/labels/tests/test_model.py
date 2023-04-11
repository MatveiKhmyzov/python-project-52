from django.test import TestCase
from task_manager.labels.models import Label


class TestLabelModel(TestCase):
    fixtures = ['labels.json']

    @classmethod
    def setUpTestData(cls):
        cls.label = Label.objects.get(pk=1)

    def test_string_representation_of_label(self):
        expected_representation_label = 'science'
        self.assertEqual(expected_representation_label, str(self.label))
