# Generated by Django 5.0.6 on 2024-05-23 06:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='members',
        ),
        migrations.RemoveField(
            model_name='messages',
            name='rasm',
        ),
        migrations.AddField(
            model_name='messages',
            name='members',
            field=models.ManyToManyField(related_name='members', to=settings.AUTH_USER_MODEL),
        ),
    ]
