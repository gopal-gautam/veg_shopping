from customer.models import Customer

__author__ = 'gopal'

from django import forms

class RegistrationForm(forms.ModelForm):
    """
    Registration form for customer to create a login account
    """
    password = forms.CharField(max_length=50, widget=forms.PasswordInput())
    class Meta:
        model = Customer
        fields = ['name', 'username', 'password']


class LoginForm(forms.ModelForm):
    """
    Login form for the customer
    """
    class Meta:
        model = Customer
        fields = ["username", "password"]
        widgets = {
            'password':forms.PasswordInput()
        }