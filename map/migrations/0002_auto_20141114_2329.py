# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='employee_count_range',
            field=models.CharField(max_length=255, null=True),
            preserve_default=True,
        ),
    ]
