from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from customer.forms import RegistrationForm, LoginForm
from customer.models import Customer


def register(request):
    """
    Register a new customer
    :param request:
    :return:
    """
    if request.method == "POST":
        register_form = RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect('/customer/login')

    args = {}
    args['register_form']=RegistrationForm()
    return render(request, 'register.html', args)


def login(request):
    """
    authenticate the login of the customer and prepare a session id
    :param request:
    :return:
    """

    #Check if the customer hasn't logged out and active within the session
    try:
        customer = Customer.objects.get(id=request.session['cust_id'])
        print "session id: %s" % request.session['cust_id']
    except:
        customer = None
    if customer is not None:
        return HttpResponseRedirect('/listTarkari')

    #process the login form and authenticate
    if request.method == "POST":
        user = LoginForm(request.POST)
        if user.is_valid():
            username = user.cleaned_data['username']
            password = user.cleaned_data['password']
            try:
                user_db = Customer.objects.get(username=username, password=password)
            except:
                return render(request, 'login.html', {"form":LoginForm(),"message":"Unknown username or password"})
            if user_db is not None:
                request.session['cust_id'] = user_db.id
                #user's logged in session is now active. Redirect the customer to view all the lists of tarkaris
                return HttpResponseRedirect('/listTarkari')

    #Request hasn't obtained, so prepare for login form display
    args = {}
    args['form']=LoginForm()
    return render(request, 'login.html',args)


def logout(request):
    """
    Destroy the logged in session of the customer
    :param request:
    :return:
    """
    request.session.delete(session_key=None)

    #Redirect to the login page
    return HttpResponseRedirect('/customer/login')