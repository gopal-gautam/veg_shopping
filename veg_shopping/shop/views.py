from django.shortcuts import render
from django.http import HttpResponseRedirect

# from .models import Tarkari, Godam, Cart, Customer, Farmer, Sales
from .forms import LoginForm

# Create your views here.


def register(request):
    if request.method == "POST":
        user = LoginForm(request.POST)
        if user.is_valid():
            request.session['cust_id'] = user.id
            return HttpResponseRedirect('/listTarkari')
    args = {}
    args['form']=LoginForm()
    return render(request,'login.html',args)








# def removeFromCart(request, cart_id, tarkari_id):
#     tarkari = Cart.objects.get(id=cart_id, tarkari=tarkari_id)
#     tarkari.delete()


# def transact(request, tarkari_id, number, customer_id, farmer_id):
#     tarkari = Tarkari.objects.get(id=tarkari_id)
#     customer = Customer.objects.get(id=customer_id)
#     farmer = Farmer.objects.get(id=farmer_id)