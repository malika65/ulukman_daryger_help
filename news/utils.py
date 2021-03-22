from django.core.mail import send_mail
from django.conf import settings

def send_to_email(message, email):
    send_mail(
        'Улукман дарыгер обращение со страницы',
        message,
        settings.EMAIL_FROM,
        [email,]
    )