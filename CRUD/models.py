from django.db import models



class Employee(models.Model):
    emp_id=models.CharField(max_length=20)
    emp_contact=models.CharField(max_length=15)
