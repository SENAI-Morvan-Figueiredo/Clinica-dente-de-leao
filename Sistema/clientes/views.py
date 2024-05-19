from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Clientes
from django.urls import reverse_lazy

class ClienteListView(ListView):
    model = Clientes
    template_name = 'cliente_list.html'

class ClienteDetailView(DetailView):
    model = Clientes
    template_name = 'cliente_detail.html'

class ClienteCreateView(CreateView):
    model = Clientes
    fields = ['nome', 'cpf', 'genero', 'convenio', 'plano', 'cep', 'rua', 'numero', 'complemento', 'municipio', 'unidade_federal', 'data_nascimento', 'data_inicio', 'is_ativo', 'user']
    template_name = 'cliente_form.html'

class ClienteUpdateView(UpdateView):
    model = Clientes
    fields = ['nome', 'cpf', 'genero', 'convenio', 'plano', 'cep', 'rua', 'numero', 'complemento', 'municipio', 'unidade_federal', 'data_nascimento', 'data_inicio', 'is_ativo', 'user']
    template_name = 'cliente_form.html'

class ClienteDeleteView(DeleteView):
    model = Clientes
    success_url = reverse_lazy('cliente-list')
    template_name = 'cliente_confirm_delete.html'
