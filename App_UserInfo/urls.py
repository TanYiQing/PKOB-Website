from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.student),
    path('victim/', views.victim),
    path('penghulu/', views.penghulu),
    path('victim_report/', views.victims_report),

]
