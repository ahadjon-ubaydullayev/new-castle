from django.shortcuts import render
from settings.views import *

def list_config(request):
    return render(request, 'register/list-config.html')


