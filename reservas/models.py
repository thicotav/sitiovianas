from django.db import models
from datetime import datetime

# Crie seus modelos aqui.
class Reserva(models.Model):

    nome_cliente = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    data_entrada = models.DateField()
    data_saida = models.DateField()

    def __str__(self):
        return f"{self.nome_cliente} - {self.data_entrada} até {self.data_saida}"

    STATUS_CHOICES = [
        ('Pendente', 'Pendente'),
        ('Confirmado', 'confirmado'),
        ('Cancelado', 'Cancelado'),
    ]
    
    Status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pendente'
    )