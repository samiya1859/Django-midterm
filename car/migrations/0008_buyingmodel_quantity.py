# Generated by Django 5.0 on 2024-01-22 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0007_buyingmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyingmodel',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
