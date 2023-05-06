from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from School_Online import settings


def send_mail(subject,context,template_name,to):
    try:
        html_message = render_to_string(context,template_name)
        plain_text = strip_tags(html_message)
        from_email = settings.EMAIL_HOST_USER
        send_mail(subject,context,plain_text,from_email,[to],html_message=html_message)
    except:
        pass