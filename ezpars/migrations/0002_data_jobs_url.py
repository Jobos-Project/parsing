# Generated by Django 2.0.7 on 2018-08-03 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ezpars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='data_jobs',
            name='url',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
