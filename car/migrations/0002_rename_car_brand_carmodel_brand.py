# Generated by Django 5.0 on 2024-01-21 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carmodel',
            old_name='car_brand',
            new_name='brand',
        ),
    ]
