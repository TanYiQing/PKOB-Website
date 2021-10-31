from django.shortcuts import render
from django.http import HttpResponse


def student(request):
    return HttpResponse("Hello My Students")

def victim(request):
    return render(request, 'App_UserInfo/victim.html')

def penghulu(request):
    name="tan yi qing"
    position="Penghulu"
    return render(request, 'App_UserInfo/penghulu.html', context={'name': name, 'position': position})

def victims_report(request):
    victim_list = ["Tan Jia Earn", "Ng Shen Meng", "Wong Fang Man"]
    return render(request, 'App_UserInfo/victim_report.html', context={'victim_list': victim_list})

