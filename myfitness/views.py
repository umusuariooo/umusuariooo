from django.shortcuts import render, redirect, get_object_or_404
from .models import myfitness
from datetime import datetime

def index(request):
    listamyfitness = myfitness.objects.all()
    return render(request, 'indexcliente.html', {'lista': listamyfitness})

def cadastro(request):
    return render(request, 'cadastromyfitness.html')

def listar(request):
    listamyfitness = myfitness.objects.all()
    return render(request, 'listarmyfitness.html', {'lista': listamyfitness})

def cadastro(request):
    return render(request, 'cadastromyfitness.html')

def criar(request):
    nome = request.POST['nome']
    sobrenome = request.POST['sobrenome']
    email = request.POST['email']
    myfitness = myfitness.objects.create(primeiro_nome=nome, sobrenome=sobrenome, email=email, status=1)

    myfitness.save()
    return redirect('indexmyfitness')

def editar(request, id_myfitness):
    myfitness = get_object_or_404(myfitness, pk=id_myfitness)
    return render(request, 'editarmyfitness.html', {'dados_myfitness': myfitness})

def atualizar_myfitness(request):
    id_myfitness = request.POST["id"]
    myfitness = myfitness.objects.get(pk=id_myfitness)
    myfitness.primeiro_nome = request.POST["nome"]
    myfitness.sobrenome = request.POST["sobrenome"]
    myfitness.email = request.POST["email"]
    myfitness.save()
    return redirect('indexmyfitness')


def deletar_myfitness(requets, id_myfitness):
    myfitness = get_object_or_404(myfitness, pk=id_myfitness)
    myfitness.delete()
    return redirect('indexmyfitness')