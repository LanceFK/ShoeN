# Generated by Django 2.2 on 2022-06-02 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShoeN', '0020_auto_20220602_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='shoe_in', max_length=255),
        ),
    ]
