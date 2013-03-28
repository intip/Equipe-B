from django.db import models

# Create your models here.
class Evento(models.Model):
    nome = models.CharField(max_length=64)
    # palestrante = 
    descricao = models.TextField()
    data = models.DateField()

    def __unicode__(self):
        return self.nome

class Pessoa(models.Model):
    __TIPO = (
        ('P', 'Palestrante'),
        ('V', 'Visitante')
    )
    nome = models.CharField(max_length=64)
    tipo = models.CharField(max_length=1, choices=__TIPO, default="P")

    def __unicode__(self):
        return self.nome

class Palestra(models.Model):
    titulo = models.CharField(max_length=256)
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    evento = models.ForeignKey(Evento)
    palestrante = models.OneToOneField(Pessoa)

    def __unicode__(self):
        return self.titulo