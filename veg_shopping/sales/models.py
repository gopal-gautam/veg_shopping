from django.db import models
from farmer.models import Farmer
from customer.models import Customer
from tarkari.models import Tarkari

# Create your models here.

class Sales(models.Model):
    farmer = models.ForeignKey(Farmer)
    customer = models.ForeignKey(Customer)
    tarkari = models.ForeignKey(Tarkari)
    number = models.IntegerField(default=0)

    def __unicode__(self):
        return self.customer.name