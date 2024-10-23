from time import time

from django.core.mail import send_mail

from root.settings import EMAIL_HOST_USER


def send_email(receiver_email , msg):
    subject = "P23 group"
    start = time()
    send_mail(subject ,msg,EMAIL_HOST_USER,recipient_list=[receiver_email,])
    end = time()
    return {"status":"Yuborildi" ,  "time": end-start , "email" :receiver_email }