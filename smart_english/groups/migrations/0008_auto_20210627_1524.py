# Generated by Django 3.1.7 on 2021-06-27 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0007_auto_20210626_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newgroup',
            name='lesson_time',
            field=models.TimeField(max_length=255),
        ),
    ]
