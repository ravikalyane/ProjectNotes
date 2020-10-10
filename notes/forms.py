from django.contrib.auth.forms import forms
from .models import Note
from tinymce.models import HTMLField
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class NotesForm(forms.ModelForm):
    note = HTMLField()

    class Meta:
        model = Note
        exclude = ['user', ]
        fields = '__all__'


class RegisterForm(UserCreationForm):
    email = forms.EmailField

    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'username', 'email', 'password1', 'password2'
