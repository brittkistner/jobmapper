# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0002_auto_20141114_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='twitter',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
    ]
