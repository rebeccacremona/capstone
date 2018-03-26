# Generated by Django 2.0.2 on 2018-03-21 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capdb', '0029_auto_20180320_1949'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='casemetadata',
            options={'ordering': ['decision_date', 'id']},
        ),
        migrations.AddIndex(
            model_name='casemetadata',
            index=models.Index(fields=['decision_date', 'id'], name='capdb_casem_decisio_84c016_idx'),
        ),
    ]