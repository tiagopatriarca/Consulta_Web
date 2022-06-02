from mailbox import NotEmptyError
from django.shortcuts import render, HttpResponse, redirect
from core.models import Pessoa, Provedor, Divida
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.



def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request,"Usuário e/ou senha errado")
            return redirect('/')


@login_required(login_url='/login/')
def consulta(request):
    pessoa = Pessoa.objects.all
    resposta = {'pessoas': pessoa}
    return render(request, 'consulta.html', resposta)

def pessoa(request):
    return render(request, 'pessoa.html')

@login_required(login_url='/login/')
def submit_pessoa(request):
    if request.POST:
       nome = request.POST.get('nome')
       cpf = request.POST.get('cpf')
       cep = request.POST.get('cep')
       rua = request.POST.get('rua')
       bairro = request.POST.get('bairro')
       n = request.POST.get('n')
       complemento = request.POST.get('complemento')
       usuario = request.user
       Pessoa.objects.create(nome_completo=nome, cpf=cpf, cep=cep, rua=rua, bairro=bairro, num=n, complemento=complemento)
       return redirect('/')
