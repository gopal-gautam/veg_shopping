from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from farmer.forms import RegisterFarmerForm, FarmerLoginForm
from farmer.models import Farmer
from godam.models import Godam


def register(request):
    """
    A function to handle the request from farmer registration form
    :param request:
    :return:
    """
    if request.method == "POST":
        register_farmer_form = RegisterFarmerForm(request.POST)
        if register_farmer_form.is_valid():
            register_farmer_form.save()
            return HttpResponseRedirect('/farmer/login')
            
    args = {}
    args['register_farmer_form']=RegisterFarmerForm()
    return render(request, 'register_farmer.html', args)


def login(request):
    """
    Authenticate the farmer and generate a farmer session
    :param request:
    :return:
    """
    farmer = None
    if request.session.has_key('farm_id'):
        try:
            farmer = Farmer.objects.get(id=request.session['farm_id'])
        except:
            pass
    if farmer is not None:
        return HttpResponseRedirect('/farmer/farmer_portal')
    if request.method == "POST":
        # print "request is post"
        farmer_login = FarmerLoginForm(request.POST)
        if farmer_login.is_valid():
            # print "farmer_login is valid"
            farmer_username = farmer_login.cleaned_data['username']
            farmer_password = farmer_login.cleaned_data['password']
            try:
                farmer_db = Farmer.objects.get(username=farmer_username, password=farmer_password)
            except:
                return render(request, 'farmer_login.html',
                              dict(farmer_login_form=FarmerLoginForm(), message="Unknown Username or password"))
            request.session['farm_id'] = farmer_db.id
            return HttpResponseRedirect('/farmer/farmer_portal')

    args = {}
    args['farmer_login_form'] = FarmerLoginForm()
    args['message'] = "Enter Username and password"
    return render(request, 'farmer_login.html',args)


def logout(request):
    request.session.delete(session_key=None)
    return HttpResponseRedirect('/farmer/login')


def farmer_portal(request):
    """
    Display a page where farmer can add tarkaris to godam and see his past transaction to the godam
    :param request:
    :return:
    """
    farmer = None
    if request.session.has_key('farm_id'):
        try:
            farmer = Farmer.objects.get(id=request.session['farm_id'])
        except:
            pass
    if farmer is None:
        return HttpResponseRedirect('/farmer/login')
    args = {}
    args['farmer']=farmer
    godam = Godam.objects.filter(farmer=farmer)
    args["lists"] = list(godam)
    return render(request, 'farmer_portal.html', args)