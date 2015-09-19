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
    """
    a function to add items to cart
    :param request:
    :param tarkari_id:
    :param number:
    :return:
    """
    # print "addToCart tarkari_id: %s number: %s" %(tarkari_id,number)

    #check if customer session is active
    customer = None
    if request.session.has_key("cust_id"):
        try:
            customer = Customer.objects.get(id=request.session.get('cust_id'))
        except:
            pass
    if customer is None:
        return HttpResponseRedirect('/customer/login')

    #Get the tarkaris instance from the database using the tarkari_id
    tarkari_ins = None
    try:
        tarkari_ins = Tarkari.objects.get(id=tarkari_id)
    except:
        return render(request, 'error.html',{'message':"Tarkari instance not applicable"})

    if tarkari_ins is None:
        return render(request, 'error.html', {'message':"Tarkari instance not applicable"})

    #Get the godam instance having the current tarkari instance and is available
    try:
        godam = Godam.objects.get(id=tarkari_id)
    except:
        return render(request, 'error.html',{'message':'Invalid Tarkari Defined'})
    number = int(number)

    #if the requested amount of tarkari is greater than the available currently, discard the process with error message
    if godam.available < number:
        return render(request, "error.html", {"message":"We don't have that much tarkari available is:"+str(godam.available)})

    #Deduct the requested quantity of tarkari from the godam and save the godam
    godam.available -= number
    godam.save()

    #create a cart containing the customer request and save it
    c = Cart(tarkari=tarkari_ins, tarkari_count=number, customer=customer)
    c.save()

    #Redirect to view other list of tarkaris
    return HttpResponseRedirect('/listTarkari')


def delete(request, cart_id):
    """
    a function to delete items from the cart and free the tarkaris that were previously held within the cart
    :param request:
    :param cart_id:
    :return:
    """

    #verify that the customer logged in session is active
    customer = None
    if request.session.has_key("cust_id"):
        try:
            customer = Customer.objects.get(id=request.session['cust_id'])
        except:
            pass
    if customer is None:
        return HttpResponseRedirect('/customer/login')

    #Get the cart instance from where item is to be returned or else throw error
    try:
        cart = Cart.objects.get(id=cart_id)
    except:
        return render(request, 'error.html', {'message':'Unable to load the cart id'})

    #get the godam instance and return the item to the godam and save the godam
    tarkari_godam = Godam.objects.get(tarkari=cart.tarkari)
    tarkari_godam.available += cart.tarkari_count
    tarkari_godam.save()

    #delete the cart instance ie delete the item on the cart
    cart.delete()

    #redirect customer to view other list of tarkaris
    return HttpResponseRedirect('/listTarkari')


def buy(request):
    """
    a function to commit the cart that will be reflected on the sales.
    :param request:
    :return:
    """

    #verify that the customer logged in session is active
    customer = None
    if request.session.has_key("cust_id"):
        try:
            customer = Customer.objects.get(id=request.session.get('cust_id'))
        except:
            pass
    if customer is None:
        return HttpResponseRedirect('/customer/login')

    #Get all the cart items that is to be bought and identify the farmer associated with the tarkari item. Save the transaction to the sales
    c = Cart.objects.filter(customer=customer)
    for cart in c:
        tarkari = Tarkari.objects.get(id=cart.tarkari.id)
        godam = Godam.objects.get(tarkari=tarkari)
        farmer = Farmer.objects.get(id=godam.farmer_id)
    #     sales = Sales.objects.get(customer=customer, tarkari=tarkari, farmer=farmer)
    # if sales is not None:
    #     sales.number += number
    # else:
        sales = Sales(tarkari=tarkari, customer=customer, farmer=farmer, number=cart.tarkari_count)
        sales.save()
        cart.delete()

    #Redirect to view all other lists of tarkaris
    return HttpResponseRedirect('/listTarkari')