# Generated by Django 4.0 on 2022-04-21 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cerulean', '0014_remove_employeeworkdetails_end_time_01_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeeworkdetails',
            name='pd_start_time_01',
            field=models.TimeField(null=True),
        ),
    ]
