# Generated by Django 5.1.4 on 2024-12-25 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0006_rename_contact_hm_contactt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hm',
            name='contactt',
            field=models.IntegerField(),
        ),
    ]