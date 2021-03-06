# Generated by Django 2.0.2 on 2018-04-16 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capdb', '0034_auto_20180413_1855'),
    ]

    operations = [
        migrations.CreateModel(
            name='SlowQuery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.TextField()),
                ('label', models.CharField(blank=True, max_length=255, null=True)),
                ('last_seen', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-last_seen'],
                'verbose_name_plural': 'Slow queries',
            },
        ),
    ]
