from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.shortcuts import redirect 
from django.contrib import messages as msg
from django.core.mail import send_mail
# Create your views here.
from plugins.sms import SMS
from plugins.email import (
    emailPlugin
)

import json


def message(request):
    try:
        data = eval(request.body)
        # if request.method == 'POST':
            # data =  request.POST.dict();
        courier =  data.get('courier')
        message =  data.get('message')
        alert = ''
        if data.get('category') == 'sms':
            if (courier != '') and (message != ''):
                sm =  SMS(to_courier=courier, message=message)
                # print(sm)
                return JsonResponse({
                    "message":sm
                })

        elif data.get('category') == 'email':
            emailPlugin(
                template_name='email_template',
                obj={'email':'anointedngeorge@gmail.com'},
                from_email='anointedngeorge@gmail.com',
                mail_subject='This',
                data={'message':f"{message}"},
                from_head='Bomach'
                )

        elif data.get('category') == 'whatsapp':
            print('whatsapp')
        return JsonResponse({'message':'Working'})
    except Exception as e:
        return JsonResponse({'message':e})