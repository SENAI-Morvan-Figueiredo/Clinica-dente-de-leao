from django.views.generic import ListView
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.views.generic import CreateView
from django.views.generic import DetailView
from .models import Clientes

class ClienteListView(ListView):
    model = Clientes
    template_name = 'cliente_list.html'  # Nome do seu template HTML para listar clientes
    context_object_name = 'clientes'  # Nome do objeto de contexto no template

class ClienteDetailView(DetailView):
    model = Clientes
    template_name = 'cliente_detail.html'  # Nome do seu template HTML para a visualização detalhada do cliente
    context_object_name = 'cliente'  # Nome do objeto de contexto que será passado para o template

class ClienteCreateView(CreateView):
    model = Clientes
    fields = ['campo1', 'campo2', ...]  # Substitua 'campo1', 'campo2', ... pelos nomes reais dos campos do seu modelo
    template_name = 'cliente_form.html'  # Substitua 'cliente_form.html' pelo nome do seu template de formulário de cliente
    success_url = '/clientes/'  # URL para redirecionar após o sucesso do envio do formulário

class ClienteUpdateView(UpdateView):
    model = Clientes
    fields = ['campo1', 'campo2', ...]  # Substitua 'campo1', 'campo2', ... pelos nomes reais dos campos do seu modelo
    template_name = 'cliente_form.html'  # Substitua 'cliente_form.html' pelo nome do seu template de formulário de cliente
    success_url = '/clientes/'  # URL para redirecionar após o sucesso do envio do formulário

class ClienteDeleteView(DeleteView):
    model = Clientes
    template_name = 'cliente_confirm_delete.html'  # Substitua 'cliente_confirm_delete.html' pelo nome do seu template de confirmação de exclusão
    success_url = reverse_lazy('cliente-list')  # URL para redirecionar após a exclusão bem-sucedida do cliente