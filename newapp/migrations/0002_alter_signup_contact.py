# Generated by Django 5.1.4 on 2024-12-23 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='contact',
            field=models.IntegerField(),
        ),
    ]
