# Generated by Django 3.2.7 on 2021-10-02 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snowballapp', '0005_auto_20211002_1642'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersmodel',
            name='recmopmt',
        ),
    ]