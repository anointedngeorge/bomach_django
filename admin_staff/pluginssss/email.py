from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.conf import settings
from django.http import HttpResponse
import os



def emailPlugin(mail_subject, from_head, from_email, template_name, obj, data):
    
    try:
        # templates/templateResponse/email_template/email_template.html
        filename = os.path.realpath(f"templates/templateResponse/email_template/{template_name}.html")
        if os.path.exists(filename):
            # return HttpResponse('Working')
            data = data
            mail_subject = mail_subject
            message = render_to_string(filename, data)
            to_email = f"{obj.get('email')}"
            email = EmailMessage(mail_subject, message, to=[to_email], from_email=f"{from_head} <{from_email}>")
            email.send()
            return "Email Sent!"
        else:
            return HttpResponse("file does not exist")

    except Exception as e:
        # print(e)
        return HttpResponse(e)