# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0005_auto_20141118_1614'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='ceo_pct_disapprove',
        ),
    ]
