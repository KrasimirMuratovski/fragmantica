# Generated by Django 4.1.3 on 2022-12-01 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0001_initial'),
        ('designers', '0007_designer_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='designer',
            name='award',
            field=models.ManyToManyField(to='awards.award'),
        ),
    ]