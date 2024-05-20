from django.shortcuts import render
from .models import *
from django.urls import reverse_lazy
from django.contrib import messages, auth
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, View, UpdateView, FormView, DetailView
from .forms import UserAdminCreationForm


class IndexView(View):
    def get(self, request):
        return render(request, 'accounts/index.html')

class Login(LoginView):
    
    model = User
    template_name = 'accounts/login.html'
    
def logout(request):
    auth.logout(request)
    return render(request, 'accounts/logged_out.html')



class RegisterView(CreateView):

    model = User
    template_name = 'accounts/singin.html'
    form_class = UserAdminCreationForm
    success_url = reverse_lazy('index')
    
    def form_valid(self, form):
        messages.info(
            self.request, "Cadastro realizado com sucesso! Faça seu login."
        )
        return super().form_valid(form)
    



login = Login.as_view()
singin = RegisterView.as_view()
index = IndexView.as_view()
