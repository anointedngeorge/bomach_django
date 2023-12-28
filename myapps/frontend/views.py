from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.conf import settings


TEMPLATE = 'mega'

def index(request, pagename='index', page_title = 'Homepage'):
    context = {}
    context['page_title'] = page_title
    return render(request, f"{TEMPLATE}/{pagename}.html", context=context)