# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime

def home(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return render_to_response('index.html')