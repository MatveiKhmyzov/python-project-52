from .models import Status
from django import forms


class StatusForm(forms.ModelForm):

    class Meta:
        model = Status
        fields = ['name']
