from django.test import TestCase
from task_manager.users.models import CustomUser
from task_manager.tasks.models import Task
from task_manager.statuses.models import Status
from task_manager.labels.models import Label
from django.urls import reverse_lazy


class TestTaskIndexView(TestCase):
    fixtures = ['users.json', 'statuses.json', 'tasks.json', 'labels.json']

    @classmethod
    def setUpTestData(cls):
        cls.user = CustomUser.objects.get(pk=1)
        cls.executor = CustomUser.objects.get(pk=2)
        cls.label = Label.objects.get(pk=2)
        cls.task1 = Task.objects.get(pk=1)
        cls.task2 = Task.objects.get(pk=2)
        cls.task7 = Task.objects.get(pk=7)
        cls.task8 = Task.objects.get(pk=8)
        cls.status = Status.objects.get(pk=1)

    def test_filter_for_status(self):
        response = self.client.get(reverse_lazy('task_list'),
                                   {'status': self.status.pk})
        self.assertEqual(response.context['tasks'].count(), 2)
        self.assertNotContains(response, self.task7.name)

        # f = Task._meta.get_field("status")
        # response = FilterSet.filter_for_field(f, "status")
        # self.assertIsInstance(response, filters.ModelChoiceFilter)
        # self.assertEqual(response.field_name, "status")

    def test_filter_for_executor(self):
        response = self.client.get(reverse_lazy('task_list'),
                                   {'executor': self.executor.pk})
        self.assertEqual(response.context['tasks'].count(), 2)
        self.assertContains(response, self.task7.name)
        self.assertContains(response, self.task8.name)

        # f = Task._meta.get_field("executor")
        # response = FilterSet.filter_for_field(f, "executor")
        # self.assertIsInstance(response, filters.ModelChoiceFilter)
        # self.assertEqual(response.field_name, "executor")

    def test_filter_for_labels(self):
        response = self.client.get(reverse_lazy('task_list'),
                                   {'labels': self.label.pk})
        self.assertEqual(response.context['tasks'].count(), 2)
        self.assertContains(response, self.task2.name)
        self.assertContains(response, self.task7.name)

        # f = Task._meta.get_field("labels")
        # print(f)
        # response = FilterSet.filter_for_field(f, "labels")
        # print(FilterSet)
        # self.assertIsInstance(response, filters.ModelMultipleChoiceFilter)
        # self.assertEqual(response.field_name, "labels")

    def test_annotation(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse_lazy('task_list'),
                                   {'only_authorized_user_tasks': True})
        self.assertEqual(response.context['tasks'].count(), 1)
        self.assertContains(response, self.task1.name)

        # self.client.force_login(self.user)
    #     queryset = Task.objects.all()
    #     # name = TaskFilter.only_authorized_user_tasks
    #     # f = TaskFilter.get_only_authorized_user_tasks(self,
    #                                                     queryset, name, True)
    #     GET = {'get_only_authorized_user_tasks': True}
    #     f = TaskFilter(GET, queryset)
    #     # print(Task.objects.all())
    #     self.assertEqual([str(p) for p in f.qs], ['read book'])
