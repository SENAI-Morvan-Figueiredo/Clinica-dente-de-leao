from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserAdminCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'name', 'email']

class CreateUserForm(forms.Form):

    class Meta:
        model = User
        fields = ('username', 'name', 'email')