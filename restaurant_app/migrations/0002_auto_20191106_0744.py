# Generated by Django 2.2.7 on 2019-11-06 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='online_delivery',
            field=models.BooleanField(default=False),
        ),
    ]
