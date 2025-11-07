from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Funcionario,Medico, Agenda, Especialidade
from .froms import *


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
    

class FuncionarioCreateView(LoginRequiredMixin, TestMixinIsAdmin, CreateView):
    model = Funcionario
    login_url = 'accounts:login'
    template_name = 'funcionarios/cadastro.html'
    # form_class = FuncionarioCreateForm
    fields =  ['nome', 'sobrenome','cpf', 'genero', 'telefone', 'cep', 'rua', 'numero', 'complemento', 'municipio', 'unidade_federal', 'data_nacimento', 'data_contratacao', 'is_medico']

    
    if Funcionario.is_medico == 1:
        success_url = reverse_lazy('funcionarios:medico_cadastro') 
    else:
        success_url = reverse_lazy('funcionarios:funcionarios_lista')

class FuncionarioListView(LoginRequiredMixin, TestMixinIsAdmin, ListView):
    
    login_url = 'accounts:login'
    template_name = 'funcionarios/funcionario_lista.html'

    def get_queryset(self):
        return Medico.objects.all().order_by('-pk')
    

class MedicoCreateView(LoginRequiredMixin, TestMixinIsAdmin, CreateView):

    model = Medico
    login_url = 'accounts:login'
    template_name = 'funcionarios/cadastro.html'
    # form_class = MedicoCreateForm
    fields = ['crm', 'funcionario', 'especialidade']
    success_url = reverse_lazy('funcionarios:medicos_lista')
    
class MedicoListView(LoginRequiredMixin, TestMixinIsAdmin, ListView):
    
    login_url = 'accounts:login'
    template_name = 'funcionarios/medico_lista.html'

    def get_queryset(self):
        return Medico.objects.all().order_by('-pk')
    
class EspecialidadeCreateView(LoginRequiredMixin, TestMixinIsAdmin, CreateView):

    model = Especialidade
    login_url = 'accounts:login'
    template_name = 'funcionarios/cadastro.html'
    fields = ['especialidade','descricao']
    success_url = reverse_lazy('funcionarios:especialidade_lista')
    
class EspecialidadeListView(LoginRequiredMixin, TestMixinIsAdmin, ListView):
    
    login_url = 'accounts:login'
    template_name = 'funcionarios/especialidade_lista.html'

    def get_queryset(self):
        return Especialidade.objects.all().order_by('-pk')


class AgendaCreateView(LoginRequiredMixin, TestMixinIsAdmin, CreateView):

    model = Agenda
    login_url = 'accounts:login'
    template_name = 'funcionarios/agenda_cadastro.html'
    fields = ['medico', 'dia', 'horario']
    success_url = reverse_lazy('funcionarios:agenda_lista')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class AgendaUpdateView(LoginRequiredMixin, TestMixinIsAdmin, UpdateView):

    model = Agenda
    login_url = 'accounts:login'
    template_name = 'medicos/agenda_cadastro.html'
    fields = ['medico', 'dia', 'horario']
    success_url = reverse_lazy('funcionarios:agenda_lista')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class AgendaDeleteView(LoginRequiredMixin, TestMixinIsAdmin, DeleteView):
    model = Agenda
    success_url = reverse_lazy('medicos:agenda_lista')
    template_name = 'form_delete.html'

    def get_success_url(self):
        messages.success(self.request, "Consulta excluída com sucesso!")
        return reverse_lazy('medicos:agenda_lista')


class AgendaListView(LoginRequiredMixin, TestMixinIsAdmin, ListView):
    
    login_url = 'accounts:login'
    template_name = 'funcionarios/agenda_lista.html'

    def get_queryset(self):
        return Agenda.objects.filter().order_by('-pk')



funcionario_cadastro = FuncionarioCreateView.as_view()
funionarios_lista = FuncionarioListView.as_view()

medico_cadastro = MedicoCreateView.as_view()
medico_lista = MedicoListView.as_view()

especialidade_cadastro = EspecialidadeCreateView.as_view()
especialidade_lista = EspecialidadeListView.as_view()

agenda_cadastro = AgendaCreateView.as_view()
agenda_atualizar = AgendaUpdateView.as_view()
agenda_lista = AgendaListView.as_view()
agenda_deletar = AgendaDeleteView.as_view()

