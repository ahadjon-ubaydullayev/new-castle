from django.shortcuts import render

def group_manage(request):
    return render(request, 'group-management/group-control.html')

def new_stage(request):
    return render(request, 'group-management/new-stage.html')

def all_groups(request):
    return render(request, 'group-management/all-group.html')

def active_attendance(request):
    return render(request, 'group-management/active-attendance.html')

def student_attendance(request):
    return render(request, 'group-management/student-attendance.html')

def label(request):
    return render(request, 'group-management/label-page.html')

def student_transfer(request):
    return render(request, 'group-management/student-transfer.html')

def transfer_journal(request):
    return render(request, 'group-management/transfer-journal.html')

def building_journal(request):
    return render(request, 'group-management/building-journal.html')

def teacher_plan(request):
    return render(request, 'group-management/teacher-plan.html')