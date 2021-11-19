from django.shortcuts import render
from django.http import HttpResponse

from App_UserInfo.models import Student


def student(request):
    return HttpResponse("Hello My Students")


def victim(request):
    return render(request, 'App_UserInfo/victim.html')


def penghulu(request):
    name = "tan yi qing"
    position = "Penghulu"
    return render(request, 'App_UserInfo/penghulu.html', context={'name': name, 'position': position})


def victims_report(request):
    student_list = Student.objects.all()
    return render(request, 'App_UserInfo/victim_report.html', context={'student_list': student_list})