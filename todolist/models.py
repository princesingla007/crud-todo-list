from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=30)
    emp=models.CharField(max_length=30)
    add=models.CharField(max_length=30)
    gender=models.CharField(max_length=30,blank=False,null=False)
