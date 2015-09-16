"""veg_shopping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from cart.models import Cart
from customer.models import Customer
from farmer.models import Farmer
from godam.models import Godam
from sales.models import Sales
from tarkari.models import Tarkari

admin.site.register(Farmer)
admin.site.register(Customer)
admin.site.register(Tarkari)
admin.site.register(Godam)
admin.site.register(Sales)
admin.site.register(Cart)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^listTarkari', 'godam.views.listTarkari'),
    url(r'^addCart/(?P<tarkari_id>\d+)/(?P<number>\d+)','cart.views.addToCart'),
    url(r'^$','shop.views.register'),
    url(r'^home','shop.views.register'),
    url(r'^report','sales.views.createReport')
]
