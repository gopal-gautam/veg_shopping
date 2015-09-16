from django.shortcuts import render
from .models import Godam

# Create your views here.

def listTarkari(request):
    tarkaris = Godam.objects.filter(available__gt=0)
    return render(request,"listTarkari.html",{"tarkaris":tarkaris})