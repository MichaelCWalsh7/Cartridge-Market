# Generated by Django 3.2.7 on 2022-01-28 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_alter_console_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='price',
        ),
    ]