from pickle import FALSE
from tkinter import CASCADE
from django.db import models
from cpf_field.models import CPFField

# Create your models here.

class Pessoa(models.Model):
    nome_completo = models.CharField(max_length=100, blank=FALSE, null=False)
    cpf = CPFField('cpf')
    cep = models.IntegerField(max_length=11, blank=FALSE, null=False)
    rua = models.CharField(max_length=100, blank=FALSE, null=False)
    bairro = models.CharField(max_length=100, blank=FALSE, null=False)
    num = models.CharField(max_length=10, verbose_name='Nº')
    complemento = models.CharField(max_length=100)
    
class Provedor(models.Model):
    provedor = models.CharField(max_length=100, blank=True, null=True)
    sigla = models.CharField(max_length=3, blank=True, null=True)

STATUS = (('Ativo',u'Divida ativa'),('Inativo',u'Divida inativa'))
EQUIP = (('S',u'SIM'),('N',u'NÃO'))

class Divida(models.Model):
    valor = models.IntegerField(max_length=100)
    status = models.CharField(max_length=16, choices=STATUS)
    cpf = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    provedor = models.ForeignKey(Provedor, on_delete=models.CASCADE)
    equipamento = models.CharField(max_length=5, choices=EQUIP)
    modelo = models.CharField(max_length=100, blank=True,null=True)
    Serial = models.CharField(max_length=100, blank=True,null=True)
    parimonio = models.CharField(max_length=100, blank=True,null=True)

def __str__(self):
    return self.cpf

def __str__(self):
    return self.provedor








