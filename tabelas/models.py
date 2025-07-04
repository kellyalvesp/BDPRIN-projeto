from django.db import models

class Especialidade(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Medico(models.Model):
    nome = models.CharField(max_length=50)
    crm = models.CharField(max_length=10)
    telefone = models.CharField(max_length=14)

    def __str__(self):
        return self.nome
