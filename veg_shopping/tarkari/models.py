from django.db import models

# Create your models here.

class Tarkari(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    expiry_day = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name