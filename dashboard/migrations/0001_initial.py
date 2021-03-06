# Generated by Django 3.2.4 on 2021-06-13 14:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('user', 'User'), ('org', 'Organization')], default='user', max_length=20)),
                ('contact', models.CharField(max_length=15)),
                ('bio', models.CharField(blank=True, max_length=500)),
                ('address', models.CharField(max_length=100)),
                ('pincode', models.CharField(max_length=15)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
