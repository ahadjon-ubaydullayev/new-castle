from django.urls import path
from settings.views import *

urlpatterns = [
    path('', home, name='home'),
    path('index/', dashboard, name='dashboard'),
    path('login/', login_request, name='login'),
    path('config/', config, name='config'),
    path('building/', building, name='building'),
    path('time/', times, name='time'),
    path('room/', room, name='room'),
    path('students/', students, name='students'),
    path('teachers/', teachers, name='teachers'),
    path('salary/', salary, name='salary'),
    path('other/', other, name='other'),
    path('other/<int:id>/', delete_other),
    path('time/<int:id>', delete_time),
    path('salary/<int:id>/', delete_salary),
    path('room/<int:id>/', delete_room),
    path('students/<int:id>/', delete_student),
    path('building/<int:id>/', delete_building),
    # path('teacher_add/', teacher_add, name='teacher_add'),
    # path('add_building/', add_building, name='add_building'),
]
