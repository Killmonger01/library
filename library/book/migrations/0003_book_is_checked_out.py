# Generated by Django 5.0.7 on 2024-08-06 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_remove_book_name_book_borrowed_by_book_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='is_checked_out',
            field=models.BooleanField(default=False),
        ),
    ]
