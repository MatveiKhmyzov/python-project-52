from django.test import TestCase
from task_manager.labels.models import Label
from task_manager.users.models import CustomUser
from django.urls import reverse_lazy
from task_manager.utils import get_data


class TestCreateLabelView(TestCase):
    fixtures = ['users.json', 'labels.json', 'tasks.json', 'statuses.json']

    @classmethod
    def setUpTestData(cls):
        cls.user = CustomUser.objects.get(pk=1)

    # @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_label_create_view_availability(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse_lazy('create_label'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'common_create_update.html')

    def test_label_create(self):
        label_data = get_data('test_labels.json')
        create_label_data = label_data['create']['fields']
        self.client.force_login(self.user)
        response = self.client.post(reverse_lazy('create_label'),
                                    create_label_data)
        label = Label.objects.get(pk=4)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(label.name, 'summer')
        self.assertRedirects(response, reverse_lazy('label_list'))


class TestUpdateLabelView(TestCase):
    fixtures = ['users.json', 'labels.json', 'tasks.json', 'statuses.json']

    @classmethod
    def setUpTestData(cls):
        cls.user = CustomUser.objects.get(pk=1)
        cls.label = Label.objects.get(pk=2)

    def test_label_update_view_availability(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse_lazy('update_label',
                                                kwargs={'pk': self.label.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'common_create_update.html')

    def test_label_update(self):
        label_data = get_data('test_labels.json')
        update_label_data = label_data['update']['fields']
        self.client.force_login(self.user)
        response = self.client.post(
            reverse_lazy('update_label',
                         kwargs={'pk': self.label.pk}),
            update_label_data
        )
        updated_label = Label.objects.get(pk=2)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(updated_label.name, 'elephant')


class TestDeleteLabelView(TestCase):
    fixtures = ['users.json', 'labels.json', 'tasks.json', 'statuses.json']

    @classmethod
    def setUpTestData(cls):
        cls.user = CustomUser.objects.get(pk=2)
        cls.label = Label.objects.get(pk=1)

    def test_label_delete(self):
        self.client.force_login(self.user)
        response = self.client.post(
            reverse_lazy('delete_label', kwargs={'pk': self.label.pk})
        )
        self.assertEqual(response.status_code, 302)
