from django.db import models

# Create your models here.
class Evento(models.Model):
    nome = models.CharField(max_length=64)
    # palestrante = 
    descricao = models.TextField()
    data = models.DateField()

# class Pessoa(models.Model):
#     nome = models.CharField(max_length=64)
#     tipo = models.CharField(max_length=30)

# class Palestra(models.Model):