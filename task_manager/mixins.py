from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.shortcuts import redirect


class RequiredLoginUserMixin(LoginRequiredMixin):
    denied_message = 'You are not authorized! Please sign in.'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.add_message(request, messages.ERROR,
                                 self.denied_message)
            return redirect('login_user')
        return super().dispatch(
            request, *args, **kwargs
        )


class CustomUserPassesTestMixin(UserPassesTestMixin):
    permission_denied_message = 'You do not have' \
                                ' rights to change another user.'

    def test_func(self):
        return self.get_object().id == self.request.user.pk

    def handle_no_permission(self):
        messages.add_message(self.request, messages.ERROR,
                             self.permission_denied_message)
        return redirect('user_list')
