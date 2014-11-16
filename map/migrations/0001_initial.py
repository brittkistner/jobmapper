# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('assigned_key', models.IntegerField(serialize=False, primary_key=True)),
                ('LICID', models.CharField(max_length=10, null=True)),
                ('GDCID', models.CharField(max_length=10, null=True)),
                ('name', models.CharField(max_length=255)),
                ('street_address', models.CharField(max_length=255, null=True)),
                ('city', models.CharField(max_length=255, null=True)),
                ('state', models.CharField(max_length=255, null=True)),
                ('zip_code', models.IntegerField(null=True)),
                ('address', models.CharField(max_length=255)),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('twitter', models.CharField(max_length=50, null=True)),
                ('logo_url', models.URLField(null=True)),
                ('description', models.TextField(null=True)),
                ('company_type', models.CharField(max_length=75, null=True)),
                ('tckr', models.CharField(max_length=10)),
                ('founded_year', models.IntegerField()),
                ('website_url', models.URLField(null=True)),
                ('employee_count_range', models.CharField(max_length=255, null=True)),
                ('stock_exchange', models.CharField(max_length=4, null=True)),
                ('num_followers', models.IntegerField(null=True)),
                ('overall_rating', models.FloatField(null=True)),
                ('rating_description', models.CharField(max_length=50, null=True)),
                ('culture_values_rating', models.FloatField(null=True)),
                ('senior_leadership_rating', models.FloatField(null=True)),
                ('compensation_benefits_rating', models.FloatField(null=True)),
                ('career_opportunities_rating', models.FloatField(null=True)),
                ('work_life_balance_rating', models.FloatField(null=True)),
                ('number_ratings', models.IntegerField(null=True)),
                ('industry', models.CharField(max_length=255, null=True)),
                ('ceo', models.CharField(max_length=255, null=True)),
                ('ceo_pct_disapprove', models.FloatField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('word', models.CharField(max_length=75)),
                ('company', models.ForeignKey(related_name='keywords', to='map.Company')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
