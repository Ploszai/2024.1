from django.contrib import admin
from .models import Colaborador
@admin.register(Colaborador)
class ColaboradorAdmin(admin.ModelAdmin):
    list_display = ('nome','email','cpf','cargo','ativo','data_criacao')
    search_fields = ('nome','email','cpf','cargo')
