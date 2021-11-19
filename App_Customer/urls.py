from django.urls import path
from . import views

urlpatterns = [
    path('customer/', views.index),
    path('<int:ic_no>', views.customer_detail, name="customer-detail"),
]
