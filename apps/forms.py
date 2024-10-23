import re

from allauth.account.forms import LoginForm
from django.core.exceptions import ValidationError
from django.forms import ModelForm, IntegerField

from apps.models import User, Order, Stream

class MyCustomLoginForm(LoginForm):
    def login(self, *args, **kwargs):
        print(10)
        # Add your own processing here.

        # You must return the original result.
        return super(MyCustomLoginForm, self).login(*args, **kwargs)

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = 'product', 'full_name', 'phone_number'

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        return re.sub('\D', '', phone_number)

class StreamForm(ModelForm):
    class Meta:
        model = Stream
        fields = 'name', 'discount', 'product' , 'owner'




