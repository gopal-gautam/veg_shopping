from django.shortcuts import render

# Create your views here.
from sales.models import Sales


def createReport(request):
    sales = Sales.objects.all()
    render(request, "salesreport.html",{"sales":sales})