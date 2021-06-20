from django.shortcuts import render

def groups(request):
    return render(request, 'groups/group.html')

def new_group(request):
    return render(request, 'groups/new-group.html')

def attendance(request):
    return render(request, 'groups/attendance.html')

def view_attendance(request):
    return render(request, 'groups/view-attendance.html')
