__author__ = 'gopal'

from django.conf.urls import include, url

urlpatterns = [
    url(r'^register','customer.views.register'),
    url(r'^login','customer.views.login'),
    url(r'^logout','customer.views.logout'),
    url(r'^$','customer.views.login'),
    url(r'^report/(?P<customer_id>\d+)','sales.views.createCustomerReport')
]
