# Generated by Django 5.0 on 2024-01-21 11:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0005_alter_carmodel_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carmodel',
            name='comments',
        ),
        migrations.AddField(
            model_name='commentmodel',
            name='car',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='car.carmodel'),
        ),
    ]
