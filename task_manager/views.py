from django.views.generic import TemplateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _
from django.urls import reverse_lazy
from django.contrib import messages


class IndexView(TemplateView):
    template_name = 'index.html'
    extra_context = {
        'browser_tab_title': _('Task Manager')
    }


class LoginUser(SuccessMessageMixin, LoginView):
    next_page = 'home'
    form_class = AuthenticationForm
    template_name = 'common_create_update.html'
    success_message = _("You are logged in")
    extra_context = {
        'browser_tab_title': _('Task Manager'),
        'page_title': _('Entrance'),
        'button_text': _('Sign in'),
    }


class LogoutUser(LogoutView):
    next_page = 'home'
    success_message = _("You are logged out")

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.add_message(request, messages.INFO, self.success_message)
        return response
