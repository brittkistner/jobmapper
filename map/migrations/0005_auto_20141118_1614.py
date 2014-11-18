# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0004_auto_20141118_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='founded_year',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
