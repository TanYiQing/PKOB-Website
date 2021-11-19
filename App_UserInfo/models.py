from django.db import models


class Student(models.Model):
    matric_no = models.CharField(primary_key=True, max_length=10, verbose_name='Matric Number')
    name = models.CharField(max_length=255, verbose_name='Name')