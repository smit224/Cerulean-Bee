# Generated by Django 4.0 on 2022-04-22 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cerulean', '0021_rename_order_date_printorder_orderdate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='printorder',
            old_name='art_date',
            new_name='artdate',
        ),
    ]
