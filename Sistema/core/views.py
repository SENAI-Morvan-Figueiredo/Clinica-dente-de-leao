from django.shortcuts import render
from django.views.generic import View
from clientes.models import Consulta

class IndexView(View):

    def get(self, request):
        return render(request, 'index.html')
    
    def get_queryset(self):
        return Consulta.objects.all().order_by('-pk')[:5]
        
    
index = IndexView.as_view()