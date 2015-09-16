# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0001_initial'),
        ('customer', '0001_initial'),
        ('tarkari', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField(default=0)),
                ('customer', models.ForeignKey(to='customer.Customer')),
                ('farmer', models.ForeignKey(to='farmer.Farmer')),
                ('tarkari', models.ForeignKey(to='tarkari.Tarkari')),
            ],
        ),
    ]
