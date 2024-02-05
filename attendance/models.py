from django.db import models
from students.models import Department
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date
from students.models import Student


# Create your models here.
class Machine(models.Model):
    machine_id = models.CharField(max_length=250,unique=True)
    branch=models.ForeignKey(Department, on_delete=models.CASCADE)
    admission_year = models.PositiveIntegerField(
            validators=[
                MinValueValidator(1900), 
                MaxValueValidator(date.today().year)],
            help_text="Use the following format: <YYYY>")

    def __str__(self):
        return self.machine_id


class Attendance_table(models.Model):
    date = models.DateField(blank=True , null=True)
    is_present  = models.BooleanField(blank=False , default=False)
    roll_no = models.CharField(max_length=250,unique=True)
    session_id= models.CharField(null=False ,max_length=20,primary_key=True)
    stud_name=models.CharField(max_length=100)
    sem_type= models.BooleanField(blank=False , default=False)

    def __str__(self):
        return f"{self.stud_name} , {self.session_id}"
