# Generated by Django 2.0.8 on 2018-10-17 18:36

import django.contrib.postgres.search
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('capdb', '0055_auto_20181016_2056'),
    ]

    operations = [
        migrations.AddField(
            model_name='casetext',
            name='tsv',
            field=django.contrib.postgres.search.SearchVectorField(blank=True, null=True),
        ),
    ]
