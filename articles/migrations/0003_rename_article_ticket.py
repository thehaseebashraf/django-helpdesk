# Generated by Django 4.0.10 on 2024-07-12 17:40

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0002_comment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Article',
            new_name='Ticket',
        ),
    ]
