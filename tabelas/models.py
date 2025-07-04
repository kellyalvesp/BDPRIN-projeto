from django.db import models

class Especialidade(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Medico(models.Model):
    nome = models.CharField(max_length=50)
    crm = models.CharField(max_length=10)
    telefone = models.IntegerField()

    def __str__(self):
        return self.nome

class Consulta(models.Model):
    data_hora = models.DateTimeField()
    observacoes = models.CharField(max_length=250)

    def __str__(self):
        return f"Consulta em {self.data_hora.strftime('%d/%m/%Y %H:%M')} - {self.observacoes}"

class Receitas(models.Model):
    observacoes = models.CharField(max_length=250)

    def __str__(self):
        return self.observacoes
