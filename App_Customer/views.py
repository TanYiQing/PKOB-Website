from django.shortcuts import render
from .models import Customer


def index(request):
    customers = Customer.objects.all()
    return render(request, 'App_Customer/index.html', context={'customers': customers})


def customer_detail(request, ic_no):
    customer = Customer.objects.get(pk=ic_no)     # pk='primary key'
    return render(request, 'App_Customer/customer_detail.html', context={'customer': customer})
