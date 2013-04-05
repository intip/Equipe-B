#coding:utf8

from django.http import HttpResponse, HttpResponseRedirect
import datetime
from django.template import Context, Template, RequestContext
from django.template import loader
from models import Evento, Palestra, Palestrante, Visitante
from forms import SubscriptionForm



def home(request):
    eventos = Evento.objects.all()
    context = RequestContext(request, {'eventos':eventos})
    template = loader.get_template('index.html')
    content = template.render(context)

    return HttpResponse(content)


def ver_evento(request, pk):
    evento = Evento.objects.get(id=pk)
    palestras = Palestra.objects.filter(evento_id=pk)
    context = RequestContext(request, {'evento':evento, 'palestras':palestras})
    template = loader.get_template('evento.html')
    content = template.render(context)

    return HttpResponse(content)


def ver_palestra(request, pk):
    palestra = Palestra.objects.get(id=pk)
    evento = Evento.objects.get(id=palestra.evento_id)
    palestrante = Palestrante.objects.get(id=palestra.palestrante_id)
    visitantes = Visitante.objects.get(palestra_id=pk)
    context = RequestContext(request, {'evento':evento, 'palestra':palestra,'palestrante':palestrante,
                                       'visitantes':visitantes})
    template = loader.get_template('palestra.html')
    content = template.render(context)

    return HttpResponse(content)

def list_by_field(request):
    """
    return the events listed by date
    """
    evento = Evento.objects.order_by(request.GET.get('type', 'data'))
    context = RequestContext(request, {'eventos':evento})
    template = loader.get_template('index.html')
    content = template.render(context)
    return HttpResponse(content)

def subscription(request,pk):
    if request.POST:
        form = SubscriptionForm(request.POST)
        if  form.is_valid():
            obj = form.save()
            return HttpResponseRedirect('/')
        else:
            template = loader.get_template("subscription_form.html")
            context = RequestContext(request, {'form':form})
            content = template.render(context)
            return HttpResponse(content)


    template = loader.get_template("subscription_form.html")
    context = RequestContext(request, {'form':SubscriptionForm})
    content = template.render(context)
    return HttpResponse(content)

