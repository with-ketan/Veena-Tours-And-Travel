# Generated by Django 5.1.4 on 2024-12-25 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0004_signup_messages_signup_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='hm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264)),
                ('email', models.EmailField(max_length=264)),
                ('contact', models.IntegerField(max_length=200)),
                ('destination', models.CharField(max_length=264)),
            ],
            options={
                'db_table': 'hm',
            },
        ),
    ]