from django.test import TestCase
from task_manager.statuses.models import Status
from task_manager.users.models import CustomUser
from django.urls import reverse_lazy
from task_manager.utils import get_data


class TestCreateStatusView(TestCase):
    fixtures = ['users.json', 'statuses.json']

    @classmethod
    def setUpTestData(cls):
        cls.user = CustomUser.objects.get(pk=1)
        cls.status = Status.objects.get(pk=1)

    # @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_status_create_view_availability(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse_lazy('create_status'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'common_create_update.html')

    def test_status_create(self):
        status_data = get_data('test_statuses.json')
        create_status_data = status_data['create']['fields']
        self.client.force_login(self.user)
        response = self.client.post(reverse_lazy('create_status'),
                                    create_status_data)
        status = Status.objects.get(pk=3)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(status.name, 'assigned')
        self.assertRedirects(response, reverse_lazy('status_list'))


class TestUpdateStatusView(TestCase):
    fixtures = ['users.json', 'statuses.json']

    @classmethod
    def setUpTestData(cls):
        cls.user = CustomUser.objects.get(pk=1)
        cls.status = Status.objects.get(pk=1)

    def test_status_update_view_availability(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse_lazy('update_status', kwargs={'pk': self.status.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                template_name='common_create_update.html')

    def test_status_update(self):
        update_data = get_data('test_statuses.json')
        update_status_data = update_data['update']['fields']
        self.client.force_login(self.user)
        response = self.client.post(
            reverse_lazy('update_status',
                         kwargs={'pk': self.status.pk}),
            update_status_data
        )
        updated_status = Status.objects.get(pk=1)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(updated_status.name, 'declined')


class TestDeleteStatusView(TestCase):
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
