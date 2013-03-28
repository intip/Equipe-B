# Create your views here.
from django.http import HttpResponse
import datetime
from django.template import Context, Template
from django.template import loader

def home(request):
    context = Context()
    template = loader.get_template('index.html')

    content = template.render(context)

    return HttpResponse(content)