from django.test import TestCase
from task_manager.users.models import CustomUser
from django.urls import reverse_lazy


class TestCreateUserView(TestCase):
    fixtures = ['users.json']

    @classmethod
    def setUpTestData(cls):
        cls.user = CustomUser.objects.get(pk=1)

    # @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_user_create_view(self):
        response = self.client.get(reverse_lazy('create_user'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'common_create_update.html')


class TestUpdateUserView(TestCase):
    fixtures = ['users.json']

    @classmethod
    def setUpTestData(cls):
        cls.user1 = CustomUser.objects.get(pk=1)
        cls.user2 = CustomUser.objects.get(pk=2)

    def test_update_yourself(self):
        self.client.force_login(self.user1)
        response = self.client.post(
            reverse_lazy('update_user', kwargs={'pk': self.user1.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                template_name='common_create_update.html')

    def test_update_by_not_login_user(self):
        response = self.client.get(
            reverse_lazy('update_user', kwargs={'pk': self.user1.pk})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login_user'))

    # @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_update_not_yourself(self):
        self.client.force_login(self.user1)
        response = self.client.post(reverse_lazy('update_user',
                                                 kwargs={'pk': self.user2.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('user_list'))


class TestDeleteUserView(TestCase):
    fixtures = ['users.json', 'statuses.json', 'tasks.json']

    @classmethod
    def setUpTestData(cls):
        cls.user1 = CustomUser.objects.get(pk=1)
        cls.user2 = CustomUser.objects.get(pk=2)
        cls.user3 = CustomUser.objects.get(pk=3)

    def test_delete_yourself(self):
        self.client.force_login(self.user3)
        response = self.client.post(
            reverse_lazy('delete_user', kwargs={'pk': self.user3.pk})
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(CustomUser.objects.filter(pk=self.user3.pk).exists())

    # @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_delete_not_yourself(self):
        self.client.force_login(self.user1)
        response = self.client.post(reverse_lazy('delete_user',
                                                 kwargs={'pk': self.user2.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(CustomUser.objects.filter(pk=self.user2.pk).exists())

    def test_delete_protected_user(self):
        self.client.force_login(self.user1)
        response = self.client.post(
            reverse_lazy('delete_user', kwargs={'pk': self.user1.pk})
        )
        self.assertEqual(response.status_code, 302)
        # self.assertTrue(self.user1.author_task_set.exists)
        self.assertTrue(CustomUser.objects.filter(pk=self.user1.pk).exists())

    def test_delete_by_not_login_user(self):
        response = self.client.get(
            reverse_lazy('delete_user', kwargs={'pk': self.user1.pk})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login_user'))


class TestLoginLogoutUser(TestCase):
    fixtures = ['users.json']

    @classmethod
    def setUpTestData(cls):
        cls.user1 = CustomUser.objects.get(pk=1)
        cls.user1.set_password('1w3R')
        cls.user1.save()

    def test_correct_login_view(self):
        self.client.logout()
        response = self.client.get(reverse_lazy('login_user'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(self.client.login(username='AlOne', password='1w3R'))
        response = self.client.post(reverse_lazy('login_user'),
                                    {'username': 'AlOne',
                                     'password': '1w3R'}, follow=True)
        self.assertRedirects(response, reverse_lazy('home'))

    def test_correct_logout(self):
        self.client.logout()
        response = self.client.post(reverse_lazy('logout_user'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse_lazy('home'))
