# Generated by Django 4.0 on 2022-04-21 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cerulean', '0011_employeeworkdetails_end_time_01_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeworkdetails',
            name='end_time_01',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='employeeworkdetails',
            name='end_time_02',
            field=models.TimeField(null=True),
        ),
    ]
