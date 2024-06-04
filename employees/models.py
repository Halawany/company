from django.db import models

class Employee(models.Model):
    """This class representing Employee table"""
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    email = models.EmailField()
    date_joined = models.DateField()
    position = models.CharField(max_length=100)
    salary = models.PositiveIntegerField() 

    def __str__(self):
        return f"{self.first_name} {self.last_name}"