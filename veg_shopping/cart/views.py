from django.http import HttpResponseRedirect
from django.shortcuts import render
from farmer.models import Farmer
from .models import Cart
from godam.models import Godam
from customer.models import Customer

# Create your views here.
from sales.models import Sales
from tarkari.models import Tarkari


def addToCart(request, tarkari_id, number):
    tarkari = Godam.objects.get(id=tarkari_id)
    number = int(number)
    if tarkari.available < number:
        return render(request, "error.html", {"message":"We don't have that much tarkari available is:"+str(tarkari.available)})
    tarkari.available = tarkari.total_number - number
    tarkari.save()
    farmer = Farmer.objects.get(id=tarkari.farmer_id)
    tarkari_ins = Tarkari.objects.get(id=tarkari_id)
    c = Cart(tarkari=tarkari_ins, tarkari_count=number)
    c.save()
    customer = Customer(cart=c, name="hardcodedName")
    customer.save()
    sales = Sales(tarkari=tarkari_ins, customer=customer, farmer=farmer, number=number)
    sales.save()
    return HttpResponseRedirect('/listTarkari')