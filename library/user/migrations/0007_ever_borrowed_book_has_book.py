# Generated by Django 5.0.7 on 2024-08-08 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_ever_borrowed_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='ever_borrowed_book',
            name='has_book',
            field=models.BooleanField(default=False),
        ),
    ]
