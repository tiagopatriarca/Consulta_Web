from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pessoa(models.Model):
    nome_completo = models.CharField(max_length=100, blank=False, null=False)
    cpf = models.CharField(max_length=11, blank=False, null=False)
    cep = models.IntegerField(max_length=11, blank=False, null=False)
    rua = models.CharField(max_length=100, blank=False, null=False)
    bairro = models.CharField(max_length=100, blank=False, null=False)
    num = models.CharField(max_length=10, verbose_name='Nº')
    complemento = models.CharField(max_length=100)
    criador = models.ForeignKey(User, on_delete=models.CASCADE)
    
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
    criador = models.ForeignKey(User, on_delete=models.CASCADE)

def __str__(self):
    return self.cpf

def __str__(self):
    return self.provedor








