from django.shortcuts import render
from .forms import TestForm
from django.views.generic.base import View


def index(request):
    return render(request, 'index.html')
