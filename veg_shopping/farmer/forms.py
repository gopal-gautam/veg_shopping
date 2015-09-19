from farmer.models import Farmer

__author__ = 'gopal'

from django import forms


class RegisterFarmerForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Farmer
        fields=['name', 'username', 'password']


class FarmerLoginForm(forms.ModelForm):
    class Meta:
        model = Farmer
        fields=["username", "password"]
        widgets = {
            'password':forms.PasswordInput()
        }
