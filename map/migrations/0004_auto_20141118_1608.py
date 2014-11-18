# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0003_auto_20141118_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='ceo_pct_disapprove',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
