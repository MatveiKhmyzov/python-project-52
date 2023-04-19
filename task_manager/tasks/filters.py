from django_filters import FilterSet, filters
from .models import Task
from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.users.models import CustomUser
from django.utils.translation import gettext as _
from django import forms


class TaskFilter(FilterSet):

    status = filters.ModelChoiceFilter(
        queryset=Status.objects.all(),
        empty_label=_("----- status not selected -----"),
    )

    executor = filters.ModelChoiceFilter(
        queryset=CustomUser.objects.all(),
        empty_label=_("--- executor not selected ---"),
    )

    labels = filters.ModelChoiceFilter(
        queryset=Label.objects.all(),
        field_name='labels',
        label=_('Label'),
        empty_label=_("------ label not selected -----"),
    )

    only_authorized_user_tasks = filters.BooleanFilter(
        widget=forms.CheckboxInput,
        method='get_only_authorized_user_tasks',
        label=_('Only your tasks')
    )

    class Meta:
        model = Task
        fields = ['status', 'executor']

    def get_only_authorized_user_tasks(self, queryset, name, value):
        if value:
            return queryset.filter(author=self.request.user)
        return queryset
