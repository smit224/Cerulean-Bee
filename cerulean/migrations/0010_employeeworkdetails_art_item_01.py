# Generated by Django 4.0 on 2022-04-21 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cerulean', '0009_employeeworkdetails_work_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeeworkdetails',
            name='art_item_01',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
