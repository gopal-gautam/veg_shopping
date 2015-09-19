from django.db import models
from customer.models import Customer
from tarkari.models import Tarkari

# Create your models here.

class Cart(models.Model):
    tarkari = models.ForeignKey(Tarkari)
    tarkari_count = models.IntegerField(default=0)
    customer = models.ForeignKey(Customer)

    def __unicode__(self):
        return self.tarkari.name