from django.shortcuts import render, redirect
from settings import servis_setting
from django.http import JsonResponse, request
from .models import *

def home(request):
    return render(request, 'home.html')

def dashboard(request):
    return render(request, 'home.html')

def login_request(request):
    return render(request, 'log-in.html')

def config(request):
    return render(request, 'config.html')

def teachers(request):
    return render(request, 'teacher.html')

def teacher_add(request):
    return render(request, 'add_teacher.html')

def salary(request):
    if request.is_ajax and request.method == 'POST':
        print(request.POST)
        if request.POST['action'] == 'add':
            servis_setting.add_edit_salary(request.POST)
            return redirect('/salary')
        elif request.POST['action'] == 'delete':
            response = servis_setting.delete_salary(request.POST)
            return JsonResponse(response, status=200, safe=False)
    if request.method == 'GET':
        if 'add' in request.GET:
            subject = Subjects.objects.all()
            lesson_pattern = Patterns.objects.all()
            lesson_type = LessonType.objects.all()
            group = Group.objects.all()
            context = {
                'subject': subject,
                'lesson_pattern': lesson_pattern,
                'lesson_type': lesson_type,
                'group': group
            }
            return render(request, 'add_salary.html', context)
        elif 'id' in request.GET:
            subject = Subjects.objects.all()
            lesson_pattern = Patterns.objects.all()
            lesson_type = LessonType.objects.all()
            group = Group.objects.all()
            context = {
                'subject': subject,
                'lesson_pattern': lesson_pattern,
                'lesson_type': lesson_type,
                'group': group,
                'salaries': servis_setting.get_salary(request.GET['id']),
            }
            return render(request, 'edit_salary.html', context=context)
        else:
            salary = Salary.objects.all()
            return render(request, 'salary.html', {'salary': salary})

def delete_salary(request, id):
    salary = Salary.objects.get(id=id)
    salary.delete()
    return redirect('/salary')

def times(request):
    if request.is_ajax and request.method == 'POST':
        print(request.POST)
        if request.POST['action'] == 'add':
            servis_setting.add_edit_time(request.POST)
            return redirect('/time')
        elif request.POST['action'] == 'delete':
            response = servis_setting.delete_time(request.POST)
            return JsonResponse(response, status=200, safe=False)
    if request.method == 'GET':
        if 'add' in request.GET:
            subject = Subjects.objects.all()
            lesson_pattern = Patterns.objects.all()
            lesson_type = LessonType.objects.all()
            group = Group.objects.all()
            context = {
                'subject': subject,
                'lesson_pattern': lesson_pattern,
                'lesson_type': lesson_type,
                'group': group
            }
            return render(request, 'add_time.html', context)
        elif 'id' in request.GET:
            subject = Subjects.objects.all()
            lesson_pattern = Patterns.objects.all()
            lesson_type = LessonType.objects.all()
            group = Group.objects.all()
            context = {
                'subject': subject,
                'lesson_pattern': lesson_pattern,
                'lesson_type': lesson_type,
                'group': group,
                'times': servis_setting.get_times(request.GET['id'])
            }
            return render(request, 'edit_time.html', context=context)
        else:
            time = Timetable.objects.all()
            return render(request, 'time.html', {'time': time})

def delete_time(request, id):
    time = Timetable.objects.get(id=id)
    time.delete()
    return redirect('/time')

# def building(request):
#     return render(request, "building.html")

# def add_building(request):
#     return render(request, "add_building.html")

def other(request):
    if request.is_ajax and request.method == 'POST':
        print(request.POST)
        if request.POST['action'] == 'add':
            servis_setting.add_edit_other(request.POST)
            return redirect('/other')
        elif request.POST['action'] == 'delete':
            response = servis_setting.delete_other(request.POST)
            return JsonResponse(response, status=200, safe=False)
    if request.method == 'GET':
        if 'add' in request.GET:
            subject = Subjects.objects.all()
            lesson_pattern = Patterns.objects.all()
            context = {
                'subject': subject,
                'lesson_pattern': lesson_pattern,
            }
            return render(request, 'add_other.html', context)
        elif 'id' in request.GET:
            subject = Subjects.objects.all()
            lesson_pattern = Patterns.objects.all()
            context = {
                'subject': subject,
                'lesson_pattern': lesson_pattern,
                'others': servis_setting.get_other(request.GET['id'])
            }
            return render(request, 'edit_other.html', context=context)
        else:
            others = Other.objects.all()
            return render(request, 'other.html', {'others': others})

def delete_other(request, id):
    other = Other.objects.get(id=id)
    other.delete()
    return redirect('/other')

def room(request):
    if request.is_ajax and request.method == 'POST':
        print(request.POST)
        if request.POST['action'] == 'add':
            servis_setting.add_edit_room(request.POST)
            return redirect('/room')
        elif request.POST['action'] == 'delete':
            response = servis_setting.delete_room(request.POST)
            return JsonResponse(response, status=200, safe=False)
    if request.method == 'GET':
        if 'add' in request.GET:
            building_name = Building.objects.all()
            room_type = RoomType.objects.all()           
            context = {
                'building_name': building_name,
                'room_type': room_type,
            }
            return render(request, 'add_room.html', context)
        elif 'id' in request.GET:
            building_name = Building.objects.all()
            room_type = RoomType.objects.all()
            context = {
                'building_name': building_name,
                'room_type': room_type,
                'rooms': servis_setting.get_room(request.GET['id']),
            }
            return render(request, 'edit_room.html', context=context)
        else:
            room = Room.objects.all()
            return render(request, 'room.html', {'room': room})

def delete_room(request, id):
    room = Room.objects.get(id=id)
    room.delete()
    return redirect('/room')

def students(request):
    if request.is_ajax and request.method == 'POST':
        print(request.POST)
        if request.POST['action'] == 'add':
            servis_setting.add_edit_student(request.POST)
            return redirect('/students')
        elif request.POST['action'] == 'delete':
            response = servis_setting.delete_student(request.POST)
            return JsonResponse(response, status=200, safe=False)
    if request.method == 'GET':
        if 'add' in request.GET:
            building = Building.objects.all()
            context = {
                'building': building,
            }
            return render(request, 'add_student.html', context)
        elif 'id' in request.GET:
            building = Building.objects.all()
            context = {
                'building': building,
                'students': servis_setting.get_student(request.GET['id']),
            }
            return render(request, 'edit_student.html', context=context)
        else:
            student = Student.objects.all()
            return render(request, 'student.html', {'student': student})

def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('/student')

def building(request):
    if request.is_ajax and request.method == 'POST':
        print(request.POST)
        if request.POST['action'] == 'add':
            servis_setting.add_edit_building(request.POST)
            return redirect('/building')
        elif request.POST['action'] == 'delete':
            response = servis_setting.delete_building(request.POST)
            return JsonResponse(response, status=200, safe=False)
    if request.method == 'GET':
        if 'add' in request.GET:
            return render(request, 'add_building.html')
        elif 'id' in request.GET:
            context = {
                'buildings': servis_setting.get_building(request.GET['id'])
            }
            return render(request, 'edit_building.html', context=context)
        else:
            building = Building.objects.all()
            return render(request, 'building.html', {'building': building})

def delete_building(request, id):
    building = Building.objects.get(id=id)
    building.delete()
    return redirect('/building')
