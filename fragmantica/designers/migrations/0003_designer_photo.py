# Generated by Django 4.1.3 on 2022-11-30 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designers', '0002_designer_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='designer',
            name='Photo',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]
