# Generated by Django 2.2 on 2021-05-17 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShoeN', '0009_auto_20210517_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='Select Shoe', max_length=255),
        ),
    ]