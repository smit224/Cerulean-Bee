# Generated by Django 3.0.5 on 2022-04-15 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cerulean', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='email_id',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
