# Generated by Django 3.1.4 on 2020-12-22 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_auto_20201222_0707'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='price',
            field=models.IntegerField(default=10000),
            preserve_default=False,
        ),
    ]
