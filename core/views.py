from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request):
    return HttpResponse('Hello Word')

def soma(request, num1, num2):
    return HttpResponse('<h1>A soma dos valores é: {}</h1>'.format(num1 + num2))
def subtracao(request, um1, um2):
    return HttpResponse('<h1>A subtração dos valores é: {}</h1>'.format(um1 - um2))
def multiplicacao(request, nu1, nu2):
    return HttpResponse('<h1>A multiplicação dos valores é: {}</h1>'.format(nu1 * nu2))
def divisao(request, nm1, nm2):
    return HttpResponse('<h1>A divisão dos valores é: {}</h1>'.format(nm1 / nm2))
