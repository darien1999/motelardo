from django.shortcuts import render
from .models import Usuario
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from dataclasses import fields, field
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    num_usuarios=Usuario.objects.all().count()
    num_visits=request.session.get('num_vistis',0)
    num_visits=request.session['num_visits']=num_visits+1
    return render(request,'index.html',context={'num_usuarios':num_usuarios, 'num_visits':num_visits},
    )
class usuarioCreateView(CreateView): 
    model = Usuario
    fields = '__all__'
class usuarioDetailView(LoginRequiredMixin,generic.DetailView): 
    model = Usuario
    success_url = reverse_lazy('usuarios')
class usuarioListView(LoginRequiredMixin,generic.ListView):  
    model = Usuario
    paginate_by = 15
    
class usuarioUpdate(LoginRequiredMixin,UpdateView):
    model = Usuario
    fields = ['nombre', 'password', 'email']

class usuarioDelete(LoginRequiredMixin,DeleteView):  
    model = Usuario
    success_url = reverse_lazy('usuarios')

def principal(request):

    return render(request,'Principal.html',
    )    

def registro(request):

    return render(request,'registro.html',
    )     
# Create your views here.
@login_required
def usuario_por_nombre(request):
    status= 'NO_CONTENT'
    list = Usuario.objects.all()
    if request.method == 'POST':
        try:
            valor = request.POST.get('Tipo')
            status = 'SEARCH'
            if Usuario.objects.all().filter(Tipo = valor).exist() ==True:
                list = Usuario.objects.all().filter(Tipo = valor)
        except:
            status = 'NOSEARCH'
    variables = {'status': status,
                 'list': list}
    return render (request, 'catalogo/usuario_por_nombre.html',variables)