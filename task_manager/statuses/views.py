from .models import Status
from .forms import StatusForm
from django.views.generic import (
    ListView,
    UpdateView,
    CreateView,
    DeleteView
)
from task_manager.mixins import (
    RequiredLoginUserMixin,
    ProtectDeletionStatusView
)
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _
from django.urls import reverse_lazy


class StatusIndex(ListView):
    model = Status
    template_name = 'statuses/index.html'
    extra_context = {
        'browser_tab_title': _('Task Manager'),
        'page_title': _('Statuses'),
    }
    context_object_name = 'statuses'
    paginate_by = 10
    ordering = ['id']


class UpdateStatus(RequiredLoginUserMixin,
                   SuccessMessageMixin,
                   UpdateView):
    model = Status
    template_name = 'common_create_update.html'
    form_class = StatusForm
    context_object_name = 'statuses'
    success_url = reverse_lazy('status_list')
    success_message = _("Status changed successfully")
    extra_context = {
                      'browser_tab_title': _('Task Manager'),
                      'page_title': _('Changing status'),
                      'button_text': _('Change'),
                    }


class CreateStatus(SuccessMessageMixin, CreateView):
    model = Status
    template_name = 'common_create_update.html'
    form_class = StatusForm
    success_url = reverse_lazy('status_list')
    success_message = _("Status created successfully")
    extra_context = {
        'browser_tab_title': _('Task Manager'),
        'page_title': _('Create status'),
        'button_text': _('Create'),
    }


class DeleteStatus(RequiredLoginUserMixin,
                   ProtectDeletionStatusView,
                   DeleteView):
    model = Status
    template_name = 'common_delete.html'
    extra_context = {'browser_tab_title': _('Task Manager'),
                     'page_title': _('Delete status')}
    success_message = _("Status deleted successfully")
    success_url = reverse_lazy('status_list')
