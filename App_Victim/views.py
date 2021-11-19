from django.http import HttpResponse
from django.shortcuts import render
import App_Victim.models
from App_Victim.models import Victim


def register(request):
    if request.method == "POST":
        ic_no = request.POST["ic_no"]
        name = request.POST["name"]
        hp_no = request.POST["hp_no"]

        victim = App_Victim.models.Victim(ic_no=ic_no, name=name, hp_no=hp_no)
        victim.save()
        respond = "{} registered as victim".format(name)
        return render(request, 'App_Victim/victimregister.html', {"status": respond})

    return render(request, 'App_Victim/victimregister.html')


def viewdata(request):
    victim_list = Victim.objects.all().order_by("name")
    return render(request, 'App_Victim/viewdata.html', context={'victim_list': victim_list})


def victim_detail(request, ic):
    victim = Victim.objects.get(pk=ic)
    if request.method == "POST":
        hp_no = request.POST["hp_no"]
        victim.hp_no = hp_no
        victim.save()
        respond = "Edit Successful"
        victim_list = Victim.objects.all().order_by("name")
        return render(request, 'App_Victim/viewdata.html', {"status": respond, 'victim_list': victim_list})

    return render(request, 'App_Victim/victimdetails.html', context={'victim': victim})


