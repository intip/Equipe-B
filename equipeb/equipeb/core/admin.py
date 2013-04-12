#coding:utf8

from django.contrib import admin
from equipeb.core.models import Evento, Palestra, Visitante, Palestrante, Subscription




class VisitanteAdmin(admin.ModelAdmin):
    model = Visitante
    list_display = ('nome',) 
    list_filter = ('nome',) 

class PalestranteAdmin(admin.ModelAdmin):
    model = Palestrante
    list_display = ('nome', 'email')
    list_filter = ('email',)

class Palestra(admin.TabularInline):
	model = Palestra
	extra = 1

class EventoAdmin(admin.ModelAdmin):
	list_filter = ['data']
	list_display = ('descricao','nome', 'data', 'imagem')
	inlines = [Palestra]

class SubscriptionAdmin(admin.ModelAdmin):
    model = Subscription
    list_filter = ['email']
    list_display = ('nome', 'email', 'telefone')

admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(Palestrante, PalestranteAdmin)
admin.site.register(Visitante, VisitanteAdmin)
admin.site.register(Evento, EventoAdmin)

