from .models import Label
from .forms import LabelForm
from django.views.generic import (
    ListView,
    UpdateView,
    CreateView,
    DeleteView
)
from task_manager.mixins import (RequiredLoginUserMixin,
                                 ProtectDeletionLabelView)
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _
from django.urls import reverse_lazy


class LabelIndex(ListView):
    model = Label
    template_name = 'labels/index.html'
    extra_context = {
        'browser_tab_title': _('Task Manager'),
        'page_title': _('Labels'),
    }
    context_object_name = 'labels'


class UpdateLabel(RequiredLoginUserMixin,
                  SuccessMessageMixin,
                  UpdateView):
    model = Label
    template_name = 'common_create_update.html'
    form_class = LabelForm
    context_object_name = 'labels'
    success_url = reverse_lazy('label_list')
    success_message = _("Label changed successfully")
    extra_context = {
        'browser_tab_title': _('Task Manager'),
        'page_title': _('Change label'),
        'button_text': _('Change'),
    }


class CreateLabel(SuccessMessageMixin, CreateView):
    model = Label
    template_name = 'common_create_update.html'
    form_class = LabelForm
    success_url = reverse_lazy('label_list')
    success_message = _("Label created successfully")
    extra_context = {
        'browser_tab_title': _('Task Manager'),
        'page_title': _('Create label'),
        'button_text': _('Create'),
    }


class DeleteLabel(RequiredLoginUserMixin,
                  ProtectDeletionLabelView,
                  DeleteView):
    model = Label
    template_name = 'common_delete.html'
    extra_context = {'page_title': _('Deleting a label')}
    success_message = _("Label deleted successfully")
    success_url = reverse_lazy('label_list')
