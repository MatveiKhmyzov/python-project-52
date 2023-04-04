from django.test import TestCase
from task_manager.statuses.models import Status
from task_manager.users.models import CustomUser
from django.urls import reverse_lazy


class TestCreateStatusView(TestCase):
    fixtures = ['users.json', 'statuses.json']

    @classmethod
    def setUpTestData(cls):
        cls.user = CustomUser.objects.get(pk=1)
        cls.status = Status.objects.get(pk=1)

    # @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_status_create_view(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse_lazy('create_status'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'common_create_update.html')


class TestUpdateUserView(TestCase):
    fixtures = ['users.json', 'statuses.json']

    @classmethod
    def setUpTestData(cls):
        cls.user = CustomUser.objects.get(pk=1)
        cls.status = Status.objects.get(pk=2)

    def test_update_yourself(self):
        self.client.force_login(self.user)
        response = self.client.post(
            reverse_lazy('update_status', kwargs={'pk': self.status.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                template_name='common_create_update.html')


class TestDeleteUserView(TestCase):
    fixtures = ['users.json', 'statuses.json']

    @classmethod
    def setUpTestData(cls):
        cls.user = CustomUser.objects.get(pk=2)
        cls.status = Status.objects.get(pk=1)

    def test_delete_yourself(self):
        self.client.force_login(self.user)
        response = self.client.post(
            reverse_lazy('delete_status', kwargs={'pk': self.user.pk})
        )
        self.assertEqual(response.status_code, 302)
