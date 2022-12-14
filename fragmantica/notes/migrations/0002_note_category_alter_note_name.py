# Generated by Django 4.1.3 on 2022-12-01 18:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='category',
            field=models.CharField(choices=[('citrus', 'Citrus'), ('musk', 'Musk'), ('amber', 'Amber'), ('woods_and_mosses', 'Woods and Mosses'), ('herbs_and_fougeres', 'Herbs and Fougeres'), ('uncategorized', 'Uncategorized')], default='amber', max_length=18),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='note',
            name='name',
            field=models.CharField(max_length=64, unique=True, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
    ]
