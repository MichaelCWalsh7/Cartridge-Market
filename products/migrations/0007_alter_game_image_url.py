# Generated by Django 3.2.9 on 2021-12-10 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20211208_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='image_url',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
