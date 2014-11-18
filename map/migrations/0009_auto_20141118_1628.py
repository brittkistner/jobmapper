# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0008_auto_20141118_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='stock_exchange',
            field=models.CharField(max_length=10, null=True),
            preserve_default=True,
        ),
    ]
