# Generated by Django 5.0 on 2025-02-16 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='price',
            field=models.FloatField(),
        ),
    ]
