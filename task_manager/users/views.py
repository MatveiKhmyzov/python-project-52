from .forms import UserForm
from .models import CustomUser
from task_manager.mixins import (CustomUserPassesTestMixin,
                                 RequiredLoginUserMixin,
                                 )
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (
                                ListView,
                                UpdateView,
                                CreateView,
                                DeleteView
                                )
from django.utils.translation import gettext as _
from django.urls import reverse_lazy
from django.contrib import messages


# menu = [
#         {'brand': {{'title': "Task Manager", 'url_name': 'about'}}},
#         {'menu': {{'title': "Users", 'url_name': 'user_list'},
#                   {'title': "Statuses", 'url_name': 'status_list'},
#                   {'title': "Tags", 'url_name': 'status_list'},
#                   {'title': "Tasks", 'url_name': 'status_list'}},
#          },
#         {'auth': {{'title': "Entrance", 'url_name': 'user_list'},
#                   {'title': "Registration", 'url_name': 'user_list'}}}
# ]


class UserIndex(ListView):
    model = CustomUser
    template_name = 'users/index.html'
    extra_context = {
        'page_title': _('Task Manager'),
        'title': _('Users'),
    }
    context_object_name = 'users'


class UpdateUser(RequiredLoginUserMixin,
                 CustomUserPassesTestMixin,
                 SuccessMessageMixin,
                 UpdateView):
    model = CustomUser
    template_name = 'users/update.html'
    form_class = UserForm
    context_object_name = 'users'
    success_url = reverse_lazy('user_list')
    success_message = _("User changed successfully")
    extra_context = {
            'page_title': _('Task Manager'),
            'title': _('Change user'),
            'button_text': _('Change'),
        }


class CreateUser(SuccessMessageMixin, CreateView):
    model = CustomUser
    template_name = 'users/update.html'
    form_class = UserForm
    success_url = reverse_lazy('login_user')
    success_message = _("User successfully registered")
    extra_context = {
        'page_title': _('Task Manager'),
        'title': _('Create user'),
        'button_text': _('Create'),
    }


class DeleteUser(RequiredLoginUserMixin,
                 CustomUserPassesTestMixin,
                 SuccessMessageMixin,
                 DeleteView):
    model = CustomUser
    template_name = 'users/delete.html'
    extra_context = {'page_title': _('Task Manager')}
    success_message = _("User deleted successfully")
    success_url = reverse_lazy('user_list')


class LoginUser(SuccessMessageMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'
    success_message = _("You are logged in")
    extra_context = {
        'page_title': _('Task Manager'),
        'title': _('Sign in'),
    }

    def get_success_url(self):
        return reverse_lazy('home')


class LogoutUser(LogoutView):
    next_page = 'home'
    success_message = _("You are logged out")

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.add_message(request, messages.INFO, self.success_message)
        return response
