from django import forms


class TestForm(forms.Form):
    your_name = forms.CharField(label='Ваше имя', max_length=50)