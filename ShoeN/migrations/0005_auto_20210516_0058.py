# Generated by Django 2.2 on 2021-05-16 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShoeN', '0004_auto_20210514_2219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wall_message',
            name='shoe_name',
        ),
        migrations.AddField(
            model_name='wall_message',
            name='header_image',
            field=models.ImageField(default='', upload_to='img/%y'),
            preserve_default=False,
        ),
    ]
