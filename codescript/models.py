from django.db import models

# Create your models here.

class Employee(models.Model):
    name=models.CharField(max_length=100)
    emp_code=models.CharField(max_length=5)
    mobile=models.CharField(max_length=10)

    def __int__(self):
        return self.name
