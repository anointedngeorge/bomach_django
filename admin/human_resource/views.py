from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect 
from django.contrib import messages as msg

# Create your views here.
from plugins.sms import (SMS)
from plugins.email import (
    emailPlugin
)


def message(request):
    try:
        if request.method == 'POST':
            data =  request.POST.dict();
            courier =  data.get('courier')
            message =  data.get('message')
            alert = ''
            if data.get('category') == 'sms':
                if (courier != '') and (message != ''):
                    sm =  SMS(to_courier=courier, message=message)
                    alert = 'sms sent!'

            elif data.get('category') == 'email':
                # print('email')
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
        msg.success(request, f"{alert}")
        return HttpResponse(f"{alert}")
    except Exception as e:
        return HttpResponse(e)