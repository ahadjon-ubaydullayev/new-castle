from django.contrib import admin
from .models import TeacherRole, GroupPattern, NewGroup


@admin.register(GroupPattern)
class GroupPatternAdmin(admin.ModelAdmin):
    list_display = ['group_pattern']


@admin.register(NewGroup)
class NewGroupAdmin(admin.ModelAdmin):
    list_display = ['group_number', 'main_teacher', 'teacher_role', 
    'examiner', 'first_lesson', 'building', 'group_room', 'group_type',
    'lesson_time', 'lesson_days', 'group_pattern', 'total_lessons', 
    'payment', 'exam_date']