# Generated by Django 2.2.9 on 2020-01-22 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserHistory',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('user_id', models.PositiveIntegerField()),
                ('case_id', models.PositiveIntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['user_id', '-date', 'case_id'],
            },
        ),
        migrations.AddIndex(
            model_name='userhistory',
            index=models.Index(fields=['user_id', 'case_id'], name='user_data_u_user_id_416078_idx'),
        ),
        migrations.AddIndex(
            model_name='userhistory',
            index=models.Index(fields=['user_id', '-date'], name='user_data_u_user_id_f887b9_idx'),
        ),
    ]
