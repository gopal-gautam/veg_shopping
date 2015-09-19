from django.shortcuts import render

# Create your views here.
from customer.models import Customer
from farmer.models import Farmer
from sales.models import Sales


def createReport(request):
    sales = Sales.objects.all()
    return render(request, "salesreport.html",{"sales":sales})


def createFarmerReport(request, farmer_id):
    try:
        farmer = Farmer.objects.get(id=farmer_id)
    except:
        return render(request, 'error.html', {'message':'Bad farmer received'})
    sales = Sales.objects.filter(farmer=farmer)
    return render(request, "salesreport.html", {"sales":sales})

def createCustomerReport(request, customer_id):
    try:
        customer = Customer.objects.get(id=customer_id)
    except:
        return render(request, 'error.html', {'message':'Bad Customer signal received'})
    sales = Sales.objects.filter(customer=customer)
    return render(request, 'salesreport.html', {'sales':sales})