from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.conf import settings

def emailPlugin(request, template_name, obj, data):
    try:
        current_site = get_current_site(request)
        # data = { 'user': obj.email, 'domain': current_site.domain, 'uid': urlsafe_base64_encode(force_bytes(obj.id)) }
        data = data
        mail_subject = 'Account Creation...'
        message = render_to_string(f"email_template/{template_name}.html", data)
        to_email = f"{obj.email}"
        test_email = 'demo@gmail.com'
        email = EmailMessage(mail_subject, message, to=[to_email], from_email=f'Bomach <{test_email}>')
        email.send()
    except Exception as e:
            print(e)