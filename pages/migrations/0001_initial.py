# Generated by Django 3.1.4 on 2020-12-22 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_comm_paragraph', models.TextField(max_length=150)),
                ('home_care_paragraph', models.TextField(max_length=150)),
                ('home_ontime_paragraph', models.TextField(max_length=150)),
                ('vision_paragraph', models.TextField(max_length=150)),
                ('about_first_paragraph', models.TextField()),
                ('about_second_paragraph', models.TextField()),
            ],
        ),
    ]
