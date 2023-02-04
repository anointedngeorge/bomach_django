from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.conf import settings

def index(request):
    message =  f'''
        Welcome to bomach 0.1. \n
        To login <a href='{settings.ADMIN_LOGIN_PATH}'>Click Admin Dashboard</a>
    '''
    return HttpResponse(message)