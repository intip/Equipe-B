# Create your views here.
from django.http import HttpResponse
import datetime
from django.template import Context, Template, RequestContext
from django.template import loader

# from core.models import Evento

def home(request):
    context = RequestContext(request)
    template = loader.get_template('index.html')

    content = template.render(context)

    return HttpResponse(content)