# Generated by Django 3.2.4 on 2021-06-10 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='name',
        ),
    ]