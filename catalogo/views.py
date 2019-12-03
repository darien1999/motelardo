from django.shortcuts import render
from .models import Usuario
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from dataclasses import fields, field


def index(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    num_usuarios=Usuario.objects.all().count()
    
    return render(request,'index.html',context={'num_usuarios':num_usuarios},
    )
class usuarioCreateView(CreateView): 
    model = Usuario
    fields = '__all__'
class usuarioDetailView(generic.DetailView): 
    model = Usuario

class usuarioListView(generic.ListView):  
    model = Usuario
    paginate_by = 15
    
class usuarioUpdate(UpdateView):
    model = Usuario
    fields = ['nombre', 'password', 'email']

class usuarioDelete(DeleteView):  
    model = Usuario
    success_url = reverse_lazy('usuarios')

def principal(request):

    return render(request,'principal.html',
    )    

def registro(request):

    return render(request,'registro.html',
    )     
# Create your views here.
