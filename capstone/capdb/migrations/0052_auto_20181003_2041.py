# Generated by Django 2.0.8 on 2018-10-03 20:41

from django.db import migrations
import partial_index


class Migration(migrations.Migration):

    dependencies = [
        ('capdb', '0051_auto_20181001_1905'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='casemetadata',
            name='capdb_casem_court_i_42eeb9_partial',
        ),
        migrations.AddIndex(
            model_name='casemetadata',
            index=partial_index.PartialIndex(fields=['court_slug', 'decision_date', 'id'], name='capdb_casem_court_s_34d559_partial', unique=True, where='jurisdiction_id IS NOT NULL AND court_id IS NOT NULL AND NOT duplicative', where_postgresql='', where_sqlite=''),
        ),
    ]