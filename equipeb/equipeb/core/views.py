# Create your views here.
from django.http import HttpResponse
import datetime
from django.template import Context, Template, RequestContext
from django.template import loader

from models import Evento, Palestra

def home(request):
    eventos = Evento.objects.all()
    context = RequestContext(request, {'eventos':eventos})
    template = loader.get_template('index.html')
    content = template.render(context)

    return HttpResponse(content)

def ver_evento(request, pk):
    evento = Evento.objects.get(id=pk)
    palestras = Palestra.objects.get(evento_id=pk)
    context = RequestContext(request, {'evento':evento, 'palestras':palestras})
    template = loader.get_template('evento.html')
    content = template.render(context)

    return HttpResponse(content)