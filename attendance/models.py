from django.db import models
from students.models import Department
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date
from students.models import Student


# Create your models here.
class Machine(models.Model):
    machine_id = models.CharField(max_length=250,unique=True)
    branch=models.CharField(max_length=250)
    admission_year = models.PositiveIntegerField(
            validators=[
                MinValueValidator(1900), 
                MaxValueValidator(date.today().year)],
            help_text="Use the following format: <YYYY>")

    def __str__(self):
        return self.machine_id


class Attendance_table(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(blank=True)
    is_present = models.BooleanField(default=False)
    roll_no = models.CharField(max_length=250, blank=True, null=True)
    session_id = models.CharField(max_length=250, blank=True, null=True)
    stud_name = models.CharField(max_length=180, blank=True)
    sem_type = models.BooleanField(default=False)
    branch=models.CharField(max_length=250, null=True)
    stud_div=models.CharField(max_length=1, blank=True)
    stud_profile=models.ImageField(upload_to="student", null=True)
    stud_email=models.EmailField(null=True)
    admission_year = models.PositiveIntegerField(
            validators=[MinValueValidator(1900)],null=True, help_text="Use the following format: <YYYY>")

    

    def __str__(self):
        return f"{self.stud_name} , {self.session_id}"
