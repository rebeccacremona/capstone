# Generated by Django 2.2.2 on 2019-07-17 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('capdb', '0072_auto_20190717_1954'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicalvolumemetadata',
            old_name='duplicate',
            new_name='legacy_duplicate',
        ),
        migrations.RenameField(
            model_name='volumemetadata',
            old_name='duplicate',
            new_name='legacy_duplicate',
        ),
    ]
