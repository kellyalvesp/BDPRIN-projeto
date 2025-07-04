from django.db import models
from django.utils import timezone

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
    data_hora = models.DateTimeField(default=timezone.now)
    observacoes = models.CharField(max_length=250)

    def __str__(self):
        return f"Consulta em {self.data_hora.strftime('%d/%m/%Y %H:%M')} - {self.observacoes}"


class Paciente(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=14)
    data_nascimento = models.DateField()
    telefone = models.IntegerField()

    def __str__(self):
        return f"{self.nome} | CPF: {self.cpf} | Nasc: {self.data_nascimento.strftime('%d/%m/%Y')}"


class Receita(models.Model):
    consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE, related_name='receitas', null=True, blank=True)
    observacoes = models.CharField(max_length=250)

    def __str__(self):
        return self.observacoes


class ReceitaMedicamento(models.Model):
    receita = models.ForeignKey(Receita, on_delete=models.CASCADE, related_name='medicamentos')
    dosagem = models.CharField(max_length=45)
    frequencia = models.CharField(max_length=45)
    duracao = models.CharField(max_length=45)

    def __str__(self):
        return f"{self.dosagem}, {self.frequencia}, {self.duracao}"


class Medicamento(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.nome} - {self.descricao}"
