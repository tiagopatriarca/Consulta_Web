from django.contrib import admin
from core.models import Pessoa, Provedor, Divida

# Register your models here.

class PessoaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_completo', 'cpf', 'rua', 'bairro', 'num')
    list_filter = ('cpf',)

class ProvedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'sigla', 'provedor')

class DividaAdmin(admin.ModelAdmin):
    list_display = ('id', 'cpf', 'provedor', 'valor', 'status')
    list_filter = ('provedor', 'cpf',)

admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Divida, DividaAdmin)
admin.site.register(Provedor, ProvedorAdmin)


