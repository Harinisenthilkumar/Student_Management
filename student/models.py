from django.db import models
from django.contrib.auth.models import User
from course.models import Course  

class Student(models.Model):
    full_name = models.CharField(max_length=100,null=True)
    mobile_number = models.CharField(max_length=15,null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)  # Foreign Key to Course
    paid_fees = models.IntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)  # One-to-One relation 

    def __str__(self):
        return self.full_name