from django.db import models
from cart.models import Cart

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=50)
    cart = models.ForeignKey(Cart)

    def __unicode__(self):
        return self.name