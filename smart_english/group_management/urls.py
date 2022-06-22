from django.urls import path
from group_management.views import *

urlpatterns = [
    path('group-manage/', group_manage, name="group-manage"),
    path('new-stage/', new_stage, name="new-stage"),
    path('all-groups/', all_groups, name="all-groups"),
    path('active-attendance/', active_attendance, name="active-attendance"),
    path('student-attendance/', student_attendance, name="student-attendance"),
    path('label-page/', label, name="label"),
    path('student-transfer/', student_transfer, name="student-transfer"),
    path('transfer-journal/', transfer_journal, name="transfer-journal"),
    path('building-journal/', building_journal, name="building-journal"),
    path('teacher-plan/', teacher_plan, name="teacher-plan"),

]