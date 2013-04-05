#coding:utf8

from django.contrib import admin
from equipeb.core.models import Evento, Palestra, Visitante, Palestrante

admin.site.register(Visitante)
admin.site.register(Palestrante)

class Palestra(admin.TabularInline):
	model = Palestra
	extra = 1

class EventoAdmin(admin.ModelAdmin):
	list_filter = ['data']
	inlines = [Palestra]


admin.site.register(Evento, EventoAdmin)
