from django.db import models


# Create your models here.
from farmer.models import Farmer
from tarkari.models import Tarkari


class Godam(models.Model):
    tarkari = models.ForeignKey(Tarkari)
    farmer = models.ForeignKey(Farmer)
    total_number = models.IntegerField(default=0)
    available = models.IntegerField(default=0)
    date_added = models.DateTimeField('Date Added')

    def __unicode__(self):
        return self.tarkari.name