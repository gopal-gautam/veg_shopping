# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
        ('tarkari', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tarkari_count', models.IntegerField(default=0)),
                ('customer', models.ForeignKey(to='customer.Customer')),
                ('tarkari', models.ForeignKey(to='tarkari.Tarkari')),
            ],
        ),
    ]
