# Generated by Django 3.1.7 on 2021-06-26 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0003_newgroup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newgroup',
            name='lesson_days',
            field=models.CharField(max_length=255),
        ),
    ]
