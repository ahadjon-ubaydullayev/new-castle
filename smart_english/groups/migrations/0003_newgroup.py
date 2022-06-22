# Generated by Django 3.1.7 on 2021-06-21 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
        ('groups', '0002_grouppattern'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_number', models.IntegerField()),
                ('first_lesson', models.TimeField()),
                ('lesson_time', models.TimeField()),
                ('lesson_days', models.DateField()),
                ('total_lessons', models.IntegerField()),
                ('payment', models.IntegerField()),
                ('exam_date', models.DateField(blank=True, null=True)),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='building', to='settings.building')),
                ('examiner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='examiner', to='settings.staff')),
                ('group_pattern', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='new_group_pattern', to='groups.grouppattern')),
                ('group_room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_room', to='settings.room')),
                ('group_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='new_group_type', to='settings.group')),
                ('main_teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_teacher', to='settings.staff')),
                ('teacher_role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_role', to='groups.teacherrole')),
            ],
        ),
    ]