# Generated by Django 5.0.7 on 2024-08-08 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_book_borrowed_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='is_checked_out',
        ),
    ]
