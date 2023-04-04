from django.test import TestCase
from task_manager.users.models import CustomUser
from task_manager.tasks.models import Task
from task_manager.statuses.models import Status
from django.urls import reverse_lazy
from task_manager.utils import get_data


class TestCreateTaskView(TestCase):
    fixtures = ['users.json', 'statuses.json', 'tasks.json']

    @classmethod
    def setUpTestData(cls):
        cls.user = CustomUser.objects.get(pk=1)
        cls.task = Task.objects.get(pk=1)
        cls.status = Status.objects.get(pk=1)

    # @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_task_create_view(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse_lazy('create_task'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'common_create_update.html')

    def test_task_create(self):
        task_data = get_data('test_tasks.json')
        create_task_data = task_data['create']['fields']

        self.client.force_login(self.user)
        response = self.client.post(reverse_lazy('create_task'),
                                    create_task_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.task.author_id, self.user.id)
        self.assertRedirects(response, reverse_lazy('task_list'))


class TestUpdateTaskView(TestCase):
    fixtures = ['users.json', 'statuses.json', 'tasks.json']

    @classmethod
    def setUpTestData(cls):
        cls.user = CustomUser.objects.get(pk=2)
        cls.task = Task.objects.get(pk=1)
        cls.status = Status.objects.get(pk=1)

    def test_task_update_view(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse_lazy('update_task', kwargs={'pk': self.task.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                template_name='common_create_update.html')

    def test_task_update(self):
        task_data = get_data('test_tasks.json')
        update_task_data = task_data['update']['fields']

        self.client.force_login(self.user)
        response = self.client.post(reverse_lazy('update_task',
                                                 kwargs={'pk': 2}),
                                    update_task_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.get(pk=2).name, update_task_data['name'])
        self.assertRedirects(response, reverse_lazy('task_list'))


class TestDeleteTaskView(TestCase):
    fixtures = ['users.json', 'statuses.json', 'tasks.json']

    @classmethod
    def setUpTestData(cls):
        cls.user = CustomUser.objects.get(pk=1)
        cls.user2 = CustomUser.objects.get(pk=2)
        cls.task = Task.objects.get(pk=1)
        cls.status = Status.objects.get(pk=1)

    def test_task_delete_by_owner(self):
        self.client.force_login(self.user)
        response = self.client.post(
            reverse_lazy('delete_task', kwargs={'pk': self.task.pk})
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(pk=self.task.pk).exists())

    def test_task_delete_by_not_owner(self):
        self.client.force_login(self.user2)
        response = self.client.post(
            reverse_lazy('delete_task', kwargs={'pk': self.task.pk})
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(pk=self.task.pk).exists())
