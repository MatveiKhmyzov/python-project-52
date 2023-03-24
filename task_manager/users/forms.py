from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    # username = forms.CharField(max_length=30,
    #                            help_text='Obligatory field.
    #                            No more than 150 characters.'
    #                            ' Letters, numbers,
    #                            and @/./+/-/_ characters only.'
    #                            )
    # password1 = forms.CharField(max_length=30,
    #                            help_text='Your password must
    #                            contain at least 3 characters.'
    #                            )

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'username')
