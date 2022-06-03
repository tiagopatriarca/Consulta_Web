from mailbox import NotEmptyError
from django.shortcuts import render, HttpResponse, redirect
from core.models import Pessoa, Provedor, Divida
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http.response import Http404
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
    id_pessoa = request.GET.get('id')
    dados = {}
    if id_pessoa:
        dados['pessoa'] = Pessoa.objects.get(id=id_pessoa)
    return render(request, 'pessoa.html', dados)

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
        id_pessoa = request.POST.get('id')
        if id_pessoa:
            try:
                Pessoa.objects.filter(id=id_pessoa).update(nome_completo=nome, 
                                                            cpf=cpf, 
                                                            cep=cep, 
                                                            rua=rua, 
                                                            bairro=bairro, 
                                                            num=n, 
                                                            complemento=complemento, 
                                                            criador=usuario)
            except:
                raise Http404()
        else:
            try:
                Pessoa.objects.create(nome_completo=nome, 
                                        cpf=cpf, 
                                        cep=cep, 
                                        rua=rua, 
                                        bairro=bairro, 
                                        num=n, 
                                        complemento=complemento, 
                                        criador=usuario)
            except:
                raise Http404()

    return redirect('/')

@login_required(login_url='/login/')
def delete_pessoa(request, id):
    usuario = request.user
    try:
        pessoa = Pessoa.objects.get(id=id)
    except:
        raise Http404()
    if usuario == pessoa.criador:
        pessoa.delete()
    else:
        raise Http404()
    return redirect('/')

###################################################################

def divida(request):
    pessoa = Pessoa.objects.all()
    prov = Provedor.objects.all()
    context = { 
        'prov': prov,
        'pessoa': pessoa,
            }
    id_divida = request.GET.get('id')
    dados = {}
    if id_divida:
        dados['divida'] = Divida.objects.get(id=id_divida)
    return render(request, 'divida.html', context)

@login_required(login_url='/login/')
def submit_divida(request):
    if request.POST:
        valor = request.POST.get('valor')
        status = request.POST.get('status')
        cpf = request.POST.get('cpf')
        provedor = request.POST.get('provedor')
        equipamento = request.POST.get('equipamento')
        serial = request.POST.get('serial')
        patrimonio = request.POST.get('patrimonio')
        usuario = request.user
        id_divida = request.POST.get('id')
        if id_divida:
            try:
                Divida.objects.filter(id=id_divida).update(valor=valor, 
                                                            status=status, 
                                                            cpf=cpf, 
                                                            provedor=provedor, 
                                                            equipamento=equipamento, 
                                                            serial=serial, 
                                                            patrimonio=patrimonio, 
                                                            criador=usuario)
            except:
                raise Http404()
        else:
            try:
                Divida.objects.create(valor=valor, 
                                        status=status, 
                                        cpf=cpf, 
                                        provedor=provedor, 
                                        equipamento=equipamento, 
                                        serial=serial, 
                                        patrimonio=patrimonio, 
                                        criador=usuario)
            except:
                raise Http404()

    return redirect('/')

@login_required(login_url='/login/')
def delete_divida(request, id):
    usuario = request.user
    try:
        divida = Divida.objects.get(id=id)
    except:
        raise Http404()
    if usuario == divida.criador:
        divida.delete()
    else:
        raise Http404()
    return redirect('/')
