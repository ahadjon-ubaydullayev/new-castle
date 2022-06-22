from django.urls import path
from groups.views import *

urlpatterns = [
    path('groups/', groups, name='groups'),
    path('new-group/', new_group, name='new-group'),
    path('attendance/', attendance, name='attendance'),
    path('view-attendance/', view_attendance, name='view-attendance'),
    path('new-group/<int:id>/', delete_group, name='delete_group'),
    path('active-group/', active_group, name='active-group'),
    path('ended-group/', ended_group, name='ended-group'),
]