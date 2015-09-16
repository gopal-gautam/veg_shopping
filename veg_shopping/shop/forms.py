__author__ = 'gopal'


from django import forms
from customer.models import Customer

class LoginForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["id", "name"]


