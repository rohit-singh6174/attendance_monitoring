from django.db import models
from django.urls import reverse


# Create your models here.
class Department(models.Model):
    branch= models.CharField(max_length=200,blank=False,unique=True)

    def __str__(self):
        return self.branch


class Student(models.Model):
    stud_roll_no = models.CharField(max_length=250,unique=True)
    stud_name=  models.CharField(max_length=100)
    stud_phone= models.CharField(max_length=12)
    stud_email=models.EmailField()
    stud_div=models.CharField(max_length=1)
    branch=models.CharField(max_length=250)
    stud_profile=models.ImageField(upload_to="student", null=True)
    finger_id=models.IntegerField()
    year_of_admission=models.IntegerField()
    
    
    def get_url(self):
        return reverse('student_profile', args=[self.stud_roll_no])
    

    def __str__(self):
        return self.stud_roll_no





