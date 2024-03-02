from django.shortcuts import render
from .models import Clientes
# Create your views here.

def index(request):
    return render(request, 'index.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def listar(request):
    lista_clientes = Clientes.objects.all()
    return render(request, 'listar.html', {'lista': lista_clientes})