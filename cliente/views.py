from django.shortcuts import render, redirect, get_object_or_404
from .models import Clientes
from datetime import datetime

def index(request):
    lista_clientes = Clientes.objects.all()
    return render(request, 'index_cliente.html', {'lista': lista_clientes})

def cadastro(request):
    return render(request, 'cadastro_cliente.html')

def listar(request):
    lista_clientes = Clientes.objects.all()
    return render(request, 'listar_cliente.html', {'lista': lista_clientes})

def cadastro(request):
    return render(request, 'cadastro_cliente.html')

def criar(request):
    nome = request.POST['nome']
    sobrenome = request.POST['sobrenome']
    email = request.POST['email']
    cliente = Clientes.objects.create(primeiro_nome=nome, sobrenome=sobrenome, email=email, status=1)

    cliente.save()
    return redirect('index_cliente')

def editar(request, id_cliente):
    cliente = get_object_or_404(Clientes, pk=id_cliente)
    return render(request, 'editar_cliente.html', {'dados_clientes': cliente})

def atualizar_cliente(request):
    id_cliente = request.POST["id"]
    cliente = Clientes.objects.get(pk=id_cliente)
    cliente.primeiro_nome = request.POST["nome"]
    cliente.sobrenome = request.POST["sobrenome"]
    cliente.email = request.POST["email"]
    cliente.save()
    return redirect('index_cliente')


def deletar_cliente(requets, id_cliente):
    cliente = get_object_or_404(Clientes, pk=id_cliente)
    cliente.delete()
    return redirect('index_cliente')