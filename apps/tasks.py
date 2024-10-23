# Create your tasks here
import time

from django.core.mail import send_mail

from apps.models import User

from celery import shared_task

from root import settings


@shared_task
def send_email(pk):
    user = User.objects.filter(pk=pk).first()
    subject = 'P21 gruppa'
    msg = 'P21 gruppa tomonidan xabar '
    start = time.time()
    send_mail(subject, msg , settings.EMAIL_HOST_USER, [user.email])
    end = time.time()
    return {"status": "Yuborildi" , "time": end-start, "email" : user.email}

