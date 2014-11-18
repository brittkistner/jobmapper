# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0002_auto_20141116_1319'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='ceo',
            field=models.CharField(max_length=255, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='company',
            name='ceo_pct_disapprove',
            field=models.FloatField(null=True),
            preserve_default=True,
        ),
    ]
