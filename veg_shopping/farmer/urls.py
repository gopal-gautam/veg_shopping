__author__ = 'gopal'

from django.conf.urls import include, url

urlpatterns = [
    url(r'^register','farmer.views.register'),
    url(r'^login','farmer.views.login'),
    url(r'^farmer_portal','farmer.views.farmer_portal'),
    url(r'^logout','farmer.views.logout'),
    url(r'^report/(?P<farmer_id>\d+)','sales.views.createFarmerReport')
]
