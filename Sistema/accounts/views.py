from django.shortcuts import render, redirect
from .models import *
from django.urls import reverse_lazy
from django.contrib import messages, auth
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from django.views.generic import CreateView, View, UpdateView, FormView, DetailView
from .forms import *


class IndexView(View):
    def get(self, request):
        return render(request, 'accounts/index.html')

class Login(LoginView):
    
    model = User
    template_name = 'accounts/login.html'
    
def logout(request):
    auth.logout(request)
    return render(request, 'index.html')


class RegisterView(CreateView):

    model = User
    template_name = 'accounts/singup.html'
    form_class = UserAdminCreationForm
    success_url = reverse_lazy('accounts:login')
    
    def form_valid(self, form):
        messages.info(
            self.request, "Cadastro realizado com sucesso! Faça seu login."
        )
        
        return super().form_valid(form)

class UpdateUserView(LoginRequiredMixin, UpdateView):

    model = User
    login_url = reverse_lazy('accounts:login')
    template_name = 'accounts/update_user.html'
    fields = ['username', 'name', 'last_name', 'email'] 
    success_url = reverse_lazy('accounts:index')

    def get_object(self):
        return self.request.user

class UpdatePasswordView(LoginRequiredMixin, FormView):

    template_name = 'accounts/password/update_password.html'
    login_url = reverse_lazy('accounts:login')
    success_url = reverse_lazy('accounts:index')
    form_class = PasswordChangeForm

    def get_form_kwargs(self):
        kwargs = super(UpdatePasswordView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        return super(UpdatePasswordView, self).form_valid(form)



login = Login.as_view()
singin = RegisterView.as_view()
index = IndexView.as_view()
update_user = UpdateUserView.as_view()
update_password = UpdatePasswordView.as_view()

