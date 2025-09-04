from django.db import models
class Colaborador(models.Model):
    nome = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    cpf = models.CharField(max_length=14, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    cargo = models.CharField(max_length=80, blank=True, null=True)
    ativo = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"%s (%s)" % (self.nome, self.email)
