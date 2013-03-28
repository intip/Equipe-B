from django.contrib import admin
from equipeb.core.models import Evento, Palestra, Visitante, Palestrante

admin.site.register(Evento)
admin.site.register(Palestra)
admin.site.register(Visitante)
admin.site.register(Palestrante)