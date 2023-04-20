from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.utils.translation import gettext as _
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.detail import SingleObjectMixin
from task_manager.users.models import CustomUser
from task_manager.labels.models import Label
from task_manager.statuses.models import Status


class RequiredLoginUserMixin(LoginRequiredMixin):
    denied_message = _('You are not authorized! Please sign in.')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.add_message(request, messages.ERROR,
                                 self.denied_message)
            return redirect('login_user')
        return super().dispatch(
            request, *args, **kwargs
        )


class CustomUserPassesTestMixin(UserPassesTestMixin):
    permission_denied_message = _('You do not have'
                                  ' rights to change another user')

    def test_func(self):
        return self.get_object().id == self.request.user.pk

    def handle_no_permission(self):
        messages.add_message(self.request, messages.ERROR,
                             self.permission_denied_message)
        return redirect('user_list')


class TaskAuthorPassesTestMixin(UserPassesTestMixin):
    permission_denied_message = _('A task can only be'
                                  ' deleted by its author')

    def test_func(self):
        return self.get_object().author == self.request.user

    def handle_no_permission(self):
        messages.add_message(self.request, messages.ERROR,
                             self.permission_denied_message)
        return redirect('task_list')


class ProtectDeletionUserView(SingleObjectMixin, View):
    model = CustomUser

    def __init__(self, **kwargs):
        super().__init__()
        self.object = None

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        try:
            self.object.delete()
            messages.add_message(request, messages.SUCCESS,
                                 _('User deleted successfully'))
            return HttpResponseRedirect(reverse_lazy('user_list'))
        except ProtectedError:
            messages.add_message(request, messages.ERROR,
                                 _('Cannot delete user because it is in use'))
            return HttpResponseRedirect(reverse_lazy('user_list'))


class ProtectDeletionLabelView(SingleObjectMixin, View):
    model = Label
    unused_labels = Label.objects.filter(tasks__isnull=True)

    def __init__(self, **kwargs):
        super().__init__()
        self.object = None

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object in self.unused_labels:
            self.object.delete()
            messages.add_message(request, messages.SUCCESS,
                                 _('Label deleted successfully'))
            return HttpResponseRedirect(reverse_lazy('label_list'))
        else:
            messages.add_message(request, messages.ERROR,
                                 _('Cannot delete label because it is in use'))
            return HttpResponseRedirect(reverse_lazy('label_list'))


class ProtectDeletionStatusView(SingleObjectMixin, View):
    model = Status
    unused_labels = Status.objects.filter(task__isnull=True)

    def __init__(self, **kwargs):
        super().__init__()
        self.object = None

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object in self.unused_labels:
            self.object.delete()
            messages.add_message(request, messages.SUCCESS,
                                 _('Status deleted successfully'))
            return HttpResponseRedirect(reverse_lazy('status_list'))
        else:
            messages.add_message(request, messages.ERROR,
                                 _('Cannot delete status because it is in use'))
            return HttpResponseRedirect(reverse_lazy('status_list'))
