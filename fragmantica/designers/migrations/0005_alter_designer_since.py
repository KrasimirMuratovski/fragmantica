# Generated by Django 4.1.3 on 2022-11-30 16:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designers', '0004_designer_since'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designer',
            name='since',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1800), django.core.validators.MaxValueValidator(2022)]),
        ),
    ]
