# Generated by Django 4.1 on 2022-09-30 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShoeN', '0040_alter_post_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
    ]