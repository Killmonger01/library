# Generated by Django 5.0.7 on 2024-08-05 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_remove_reader_first_name_remove_reader_last_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name='Имяz'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
