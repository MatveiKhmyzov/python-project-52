from .forms import TaskForm
from .models import Task
from task_manager.mixins import (RequiredLoginUserMixin,
                                 TaskAuthorPassesTestMixin)
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (
                                ListView,
                                UpdateView,
                                CreateView,
                                DeleteView
                                )
from django.utils.translation import gettext as _
from django.urls import reverse_lazy


class TaskIndex(ListView):
    model = Task
    template_name = 'tasks/index.html'
    extra_context = {
        'page_title': _('Task Manager'),
        'title': _('Tasks'),
    }
    context_object_name = 'tasks'
    ordering = ['id']


class CreateTask(SuccessMessageMixin, CreateView):
    model = Task
    template_name = 'common_create_update.html'
    form_class = TaskForm
    success_url = reverse_lazy('task_list')
    success_message = _("Task created successfully")
    extra_context = {
        'page_title': _('Task Manager'),
        'title': _('Create task'),
        'button_text': _('Create task'),
    }

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        return super().form_valid(form)


class UpdateTask(RequiredLoginUserMixin,
                 SuccessMessageMixin,
                 UpdateView):
    model = Task
    template_name = 'common_create_update.html'
    form_class = TaskForm
    context_object_name = 'tasks'
    success_url = reverse_lazy('task_list')
    success_message = _("Task changed successfully")
    extra_context = {
            'page_title': _('Task Manager'),
            'title': _('Change task'),
            'button_text': _('Change'),
        }


class DeleteTask(RequiredLoginUserMixin,
                 TaskAuthorPassesTestMixin,
                 SuccessMessageMixin,
                 DeleteView):
    model = Task
    template_name = 'common_delete.html'
    extra_context = {'page_title': _('Task Manager')}
    success_message = _('Task deleted successfully')
    success_url = reverse_lazy('task_list')
    redirect_field_name = 'task_list'
