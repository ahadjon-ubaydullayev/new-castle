from django.contrib import admin
from .models import Timetable, UserProfile, Building, Salary, Staff, Other, Room, Student, Subjects
from .models import LessonType, Group, Patterns, RoomType, TeacherRole, TeacherTypes


@admin.register(TeacherRole)
class TeacherRoleAdmin(admin.ModelAdmin):
    list_display = ['role']


@admin.register(TeacherTypes)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['teacher_rank', 'role', 'employees', 'added_time']


@admin.register(Patterns)
class PatternsAdmin(admin.ModelAdmin):
    list_display = ['patterns']


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['group_type']


@admin.register(LessonType)
class LessonTypeAdmin(admin.ModelAdmin):
    list_display = ['lesson_types']


@admin.register(Subjects)
class SubjectsAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['building_name', 'room_number', 'room_type', 'owner']


@admin.register(RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ['type']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'middle_name', 'last_name', 'id_code', 'register_date', 'born_date', 'student_age', 'document_type',
    'id_number', 'level', 'free_time', 'id_card_number', 'address', 'building_name', 'tel_number',
    'student_login', 'student_password', 'status']


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']

@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):
    list_display = [
        'subject_name', 'lesson_pattern', 'lesson_type', 
        'group_type', 'start_time', 'finish_time'
                   ]

@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'room_amount', 'nickname', 'added_time']


@admin.register(Salary)
class SalaryAdmin(admin.ModelAdmin):
    list_display = [
        'subject_name', 'lesson_pattern', 'lesson_type', 
        'group_type', 'month_amount', 'monthly_fee',
        ]
    #order_by attribute should be added


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = [
        'first_name', 'middle_name', 'last_name', 'id_code', 'id_card_number', 'gender', 'register_date', 'born_date',
        'document_type', 'passport_id', 'role', 'workplace', 'login',
        'password',
    ]


@admin.register(Other)
class OtherAdmin(admin.ModelAdmin):
    list_display = [
        'subject_name', 'lesson_pattern', 'weekly_plan',
        'monthly_plan', 'total_lessons', 'course_duration',
    ]