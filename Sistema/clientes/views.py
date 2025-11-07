from django.db import IntegrityError
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from .models import *
from .forms import *


class TestMixinIsAdmin(UserPassesTestMixin):
    def test_func(self):
        is_admin_or_is_staff = self.request.user.is_superuser or \
            self.request.user.is_staff
        return bool(is_admin_or_is_staff)

    def handle_no_permission(self):
        messages.error(
            self.request, "Você não tem permissões!"
        )
        return redirect("accounts:index")

class ClienteCreateView(LoginRequiredMixin ,CreateView):
    
    model = Cliente
    template_name = 'clientes/cadastro.html'
    form_class = ClienteForm
    success_url = reverse_lazy('index')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    
    def get_endereco(self):
        pass
    
class ClienteUpdateView(LoginRequiredMixin, UpdateView):

    model = Cliente
    login_url = reverse_lazy('accounts:login')
    template_name = 'accounts/update_user.html'
    fields = ['cpf', 'genero', 'telefone', 'convenio', 'plano', 'cep', 'rua', 'numero', 'complemento', 'municipio', 'unidade_federal', 'data_nacimento']


    success_url = reverse_lazy('accounts:index')

    def get_object(self):
        user = self.request.user
        try:
            return Cliente.objects.get(user=user)
        except Cliente.DoesNotExist:
            return None
        
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class ClienteListView(LoginRequiredMixin, TestMixinIsAdmin, ListView):
    model = Cliente
    login_url = 'accounts:login'
    template_name = 'clientes/cliente_lista.html'

    def get_queryset(self):
        return self.model.objects.all().order_by('-pk')
    
class ConvenioCreateView(LoginRequiredMixin ,CreateView):
    
    model = Convenio
    template_name = 'clientes/cadastro.html'
    form_class = ConvenioForm
    success_url = reverse_lazy('index')
    # success_url = reverse_lazy('clientes:cadastro_plano')

    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        
class PlanoCreateView(LoginRequiredMixin ,CreateView):
    
    model = PlanoConvenio
    template_name = 'clientes/cadastro.html'
    form_class = PlanoForm
    success_url = reverse_lazy('index')
    # success_url = reverse_lazy('clientes:cadastro_planos')

    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class ConveioListView(LoginRequiredMixin, TestMixinIsAdmin, ListView):
    
    login_url = 'accounts:login'
    template_name = 'clientes/convenio_lista.html'

    def get_queryset(self):
        return Convenio.objects.all().order_by('-pk')
    
class PlanosListView(LoginRequiredMixin, TestMixinIsAdmin, ListView):
    
    login_url = 'accounts:login'
    template_name = 'medicos/lista.html'
    
    def get_queryset(self, request):
        return Convenio.objects.filter(request).order_by('-pk')

class ConsultaCreateView(LoginRequiredMixin, CreateView):

    model = Consulta
    login_url = 'accounts:login'
    template_name = 'clientes/cadastro.html'
    fields = ['agenda']
    success_url = reverse_lazy('clientes:consulta_list')
    
    def form_valid(self, form):
        try:
            form.instance.cliente = Cliente.objects.get(user=self.request.user)
            form.save()
        except IntegrityError as e:
            if 'UNIQUE constraint failed' in e.args[0]:
                messages.warning(self.request, 'Você não pode marcar esta consulta')
                return HttpResponseRedirect(reverse_lazy('clientes:consulta_create'))
        except Cliente.DoesNotExist:
            messages.warning(self.request, 'Complete seu cadastro')
            return HttpResponseRedirect(reverse_lazy('clientes:cliente_cadastro'))
        messages.info(self.request, 'Consulta marcada com sucesso!')
        return HttpResponseRedirect(reverse_lazy('clientes:consulta_list'))
    
class ConsultaUpdateView(LoginRequiredMixin, UpdateView):

    model = Consulta
    login_url = 'accounts:login'
    template_name = 'clientes/cadastro.html'
    fields = ['agenda']
    success_url = reverse_lazy('clientes:consulta_lista')
    
    def form_valid(self, form):
        form.instance.cliente = Cliente.objects.get(user=self.request.user)
        return super().form_valid(form)
    
class ConsultaDeleteView(LoginRequiredMixin, DeleteView):
    model = Consulta
    success_url = reverse_lazy('clientes:consulta_list')
    template_name = 'form_delete.html'

    def get_success_url(self):
        messages.success(self.request, "Consulta excluída com sucesso!")
        return reverse_lazy('clientes:consulta_list')


class ConsultaListView(LoginRequiredMixin, ListView):
    
    login_url = 'accounts:login'
    template_name = 'clientes/consulta_lista.html'

    def get_queryset(self):
        user=self.request.user
        try:
            cliente = Cliente.objects.get(user=user)
        except Cliente.DoesNotExist:
            messages.warning(self.request, 'Crie uma Consulta')
            return None
        try:
            consultas = Consulta.objects.filter(cliente=cliente).order_by('-pk')
        except Consulta.DoesNotExist:
            messages.warning(self.request, 'Crie uma Consulta')
            return None
        return consultas


cliente_cadastro = ClienteCreateView.as_view()
cliente_atualizar = ClienteUpdateView.as_view()
cliente_lista = ClienteListView.as_view()

convenio_cadatrar = ConvenioCreateView.as_view()
convenio_lista = ConveioListView.as_view()
plano_lista = PlanosListView.as_view()

consulta_cadastro = ConsultaCreateView.as_view()
consulta_lista = ConsultaListView.as_view()
consulta_atualizar = ConsultaUpdateView.as_view()
consulta_excluir = ConsultaDeleteView.as_view()