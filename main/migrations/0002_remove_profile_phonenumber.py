# Generated by Django 4.1.3 on 2023-07-06 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='phoneNumber',
        ),
    ]
