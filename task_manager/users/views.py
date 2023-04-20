from .forms import UserForm
from .models import CustomUser
from ..mixins import (
    CustomUserPassesTestMixin,
    RequiredLoginUserMixin,
    ProtectDeletionUserView
)
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (
    ListView,
    UpdateView,
    CreateView,
    DeleteView
)
from django.utils.translation import gettext as _
from django.urls import reverse_lazy


class UserIndex(ListView):
    model = CustomUser
    template_name = 'users/index.html'
    extra_context = {
        'browser_tab_title': _('Task Manager'),
        'page_title': _('Users'),
    }
    context_object_name = 'users'
    paginate_by = 10
    ordering = ['id']


class UpdateUser(RequiredLoginUserMixin,
                 CustomUserPassesTestMixin,
                 SuccessMessageMixin,
                 UpdateView):
    model = CustomUser
    template_name = 'common_create_update.html'
    form_class = UserForm
    context_object_name = 'users'
    success_url = reverse_lazy('user_list')
    success_message = _("User changed successfully")
    extra_context = {
        'browser_tab_title': _('Task Manager'),
        'page_title': _('Changing user'),
        'button_text': _('Change'),
    }


class CreateUser(SuccessMessageMixin, CreateView):
    model = CustomUser
    template_name = 'common_create_update.html'
    form_class = UserForm
    success_url = reverse_lazy('login_user')
    success_message = _("User successfully registered")
    extra_context = {
        'browser_tab_title': _('Task Manager'),
        'page_title': _('Registration'),
        'button_text': _('Register'),
    }


class DeleteUser(RequiredLoginUserMixin,
                 CustomUserPassesTestMixin,
                 ProtectDeletionUserView,
                 DeleteView):
    model = CustomUser
    template_name = 'common_delete.html'
    extra_context = {'browser_tab_title': _('Task Manager'),
                     'page_title': _('Deleting a user')}
    success_message = _("User deleted successfully")
    success_url = reverse_lazy('user_list')

    # def form_invalid(self, form):
    #     messages.error(self.request, self.error_message)
    #     return super().form_invalid(form)
