# Generated by Django 4.1.3 on 2022-12-01 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designers', '0006_rename_photo_designer_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='designer',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]