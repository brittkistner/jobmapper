# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0006_remove_company_ceo_pct_disapprove'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='ceo_2',
            field=models.CharField(max_length=255, null=True),
            preserve_default=True,
        ),
    ]
