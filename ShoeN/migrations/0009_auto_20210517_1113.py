# Generated by Django 2.2 on 2021-05-17 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShoeN', '0008_post_post_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='Nike', max_length=255),
        ),
    ]
