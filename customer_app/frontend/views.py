from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    message =  '''
        Welcome to bomach 0.1. \n
        To login <a href='/admin'>Click Customer Dashboard</a>
    '''
    return HttpResponse(message)