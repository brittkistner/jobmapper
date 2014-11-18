# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0007_company_ceo_2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='ceo_2',
        ),
        migrations.AddField(
            model_name='company',
            name='ceo_image',
            field=models.URLField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='company',
            name='ceo_num_rating',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='company',
            name='ceo_pct_approve',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='company',
            name='ceo_pct_disapprove',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
