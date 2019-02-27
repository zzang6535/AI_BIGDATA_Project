from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import EmailField


class LoginForm(AuthenticationForm):
    userid = EmailField(widget=forms.EmailInput(attrs={'autofocus': True}))


class LoadForm(forms.Form) :
    filename = forms.CharField(label = 'filename', max_length = 100)
