from django.db import models

# Create your models here.
class Evento(models.Model):
    nome = models.CharField(max_length=64)
    # palestrante = 
    descricao = models.TextField()
    data = models.DateField()

    def __unicode__(self):
        return self.nome

class Palestrante(models.Model):
    nome = models.CharField(max_length=64)
    email = models.EmailField()

    def __unicode__(self):
        return self.nome

class Palestra(models.Model):
    titulo = models.CharField(max_length=256)
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    evento = models.ForeignKey(Evento)
    palestrante = models.OneToOneField(Palestrante)

    def __unicode__(self):
        return self.titulo

class Visitante(models.Model):
    nome = models.CharField(max_length=64)
    palestra = models.ForeignKey(Palestra)
    def __unicode__(self):
        return self.nome



