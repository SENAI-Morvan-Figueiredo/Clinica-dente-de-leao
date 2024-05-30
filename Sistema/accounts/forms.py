from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserAdminCreationForm(UserCreationForm):

    class Meta:
        model = User
        if  User.is_superuser == 1:
            fields = ['username', 'name', 'last_name', 'email', 'is_staff', 'is_superuser']
        elif User.is_staff == 1:
            fields = ['username', 'name', 'last_name', 'email', 'is_staff']
        else:
            fields = ['username', 'name', 'last_name', 'email']
            

class UserAdminForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'is_active', 'is_staff']

class UserUpdadeForm(forms.Form):
        
    class Meta:
        model = User
        fields = UserAdminCreationForm.Meta.fields