from django.urls import path
from register.views import *

urlpatterns = [
    path('list-config/', list_config, name="list-config"),
    path('student/', students, name="students"),
    path('building/', building, name="building"), # assigned path should be fixed

]