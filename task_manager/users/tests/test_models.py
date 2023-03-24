from django.test import TestCase
from task_manager.users.models import CustomUser


class TestCustomUserModel(TestCase):
    fixtures = ['users.json']

    @classmethod
    def setUpTestData(cls):
        cls.user = CustomUser.objects.get(pk=1)

    def test_string_representation_of_customuser(self):
        expected_represenatation_customuser = 'Alan Fisker'
        self.assertEqual(expected_represenatation_customuser, str(self.user))
