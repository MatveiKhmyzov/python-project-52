from .models import Task
from django import forms
from django.utils.translation import gettext as _


class TaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['status'].empty_label = _('Status not selected')
        self.fields['executor'].empty_label = _('Executor not selected')

    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels']
