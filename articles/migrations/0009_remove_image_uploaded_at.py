# Generated by Django 4.0.10 on 2024-07-31 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='uploaded_at',
        ),
    ]
