from django.http import HttpResponseRedirect
from django.shortcuts import render
from cart.models import Cart
from customer.models import Customer
from farmer.models import Farmer
from .models import Godam

# Create your views here.
from tarkari.models import Tarkari


def listTarkari(request):
    """
    List all the available tarkaris at the godam. Requires user login to view
    :param request:
    :return: listTarkari.html
    """
    customer = None

    #Validate the logged-in status of customer
    if request.session.has_key('cust_id'):
        try:
            customer = Customer.objects.get(id=request.session['cust_id'])
        except:
            pass

    if customer is None:
        return HttpResponseRedirect('/customer/login')

    #Get the tarkaris that is available
    tarkaris = Godam.objects.filter(available__gt=0)

    #Get the carts of Logged in Customer
    cart_items = Cart.objects.filter(customer=customer)
    return render(request,"listTarkari.html",{"tarkaris":tarkaris,"customer":customer,"carts":cart_items})


def addTarkari(request):
    """
    A function to add tarkari to the godam by the farmer
    :param request:
    :return:
    """
    farmer = None

    #Validate the logged in status of farmer
    if request.session.has_key('farm_id'):
        try:
            farmer = Farmer.objects.get(id=request.session['farm_id'])
        except:
            # print "no farm session got"
            pass

    if farmer is None:
        return HttpResponseRedirect('/farmer/login')

    #Get the farmer request to add the tarkari to Godam
    if request.method == "POST":
        #identify the tarkari
        tarkari = None
        try:
            tarkari = Tarkari.objects.get(name=request.POST['tarkari_name'])
        except:
            pass

        if tarkari is None:
            print "tarkari is non here"
            name = request.POST['tarkari_name']
            price = request.POST['tarkari_price']
            expiry_day = request.POST['tarkari_expiry_day']
            tarkari = Tarkari(name=name,price=price,expiry_day=expiry_day)
            tarkari.save()

        tarkari_quantity = request.POST['tarkari_quant']

        #Update the godam
        godam_tarkari = None
        try:
            godam_tarkari = Godam.objects.get(tarkari=tarkari, farmer=farmer)
        except:
            pass

        if godam_tarkari is None:
            # print "godam_tarkari is none here"
            godam = Godam(tarkari=tarkari, farmer=farmer, total_number=tarkari_quantity, available=tarkari_quantity)
            godam.save()

        else:
            godam_tarkari.total_number += tarkari_quantity
            godam_tarkari.available += tarkari_quantity
            godam_tarkari.save()

    #Return to farmer_portal
    return HttpResponseRedirect('/farmer/farmer_portal')