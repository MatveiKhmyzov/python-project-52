from .forms import TaskForm
from .models import Task
from .models import Label
from .filters import TaskFilter
from django_filters.views import FilterView
from task_manager.mixins import (
    RequiredLoginUserMixin,
    TaskAuthorPassesTestMixin
)
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (
    UpdateView,
    CreateView,
    DeleteView,
    DetailView
)
from django.utils.translation import gettext as _
from django.urls import reverse_lazy


class TaskIndex(FilterView):
    model = Task
    template_name = 'tasks/index.html'
    extra_context = {
        'browser_tab_title': _('Task Manager'),
        'page_title': _('Tasks'),
        'button_text': _('Show'),
    }
    context_object_name = 'tasks'
    ordering = ['id']
    filterset_class = TaskFilter
    paginate_by = 10
    strict = False


class TaskCard(DetailView):
    model = Task
    template_name = 'tasks/task_card.html'
    extra_context = {
        'browser_tab_title': _('Task Manager'),
        'page_title': _('Task view'),
    }
    context_object_name = 'task'


class CreateTask(SuccessMessageMixin, CreateView):
    model = Task
    template_name = 'common_create_update.html'
    form_class = TaskForm
    success_url = reverse_lazy('task_list')
    success_message = _("Task created successfully")
    extra_context = {
        'browser_tab_title': _('Task Manager'),
        'page_title': _('Create task'),
        'button_text': _('Create'),
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
        'browser_tab_title': _('Task Manager'),
        'page_title': _('Changing task'),
        'button_text': _('Change'),
    }


class DeleteTask(RequiredLoginUserMixin,
                 TaskAuthorPassesTestMixin,
                 SuccessMessageMixin,
                 DeleteView):
    model = Task
    template_name = 'common_delete.html'
    extra_context = {'browser_tab_title': _('Deleting a task')}
    success_message = _('Task deleted successfully')
    success_url = reverse_lazy('task_list')
    redirect_field_name = 'task_list'
    unused_labels = Label.objects.filter(tasks__isnull=True)
