from django.db import models
from accounts.models import Account
from attendance.models import Machine
from students.models import Department
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Lecture_Session(models.Model):
    session_id  = models.CharField(null=False, max_length=20,primary_key=True)
    is_active  = models.BooleanField(blank=False , default=False)
    subject_name = models.CharField(null = False,max_length=30)
    email=models.EmailField(max_length=100)
    start_time = models.TimeField(default='00:00:00')
    end_time = models.TimeField(default='00:00:00')
    sem_type = models.BooleanField(default=False)
    date = models.DateField(blank=True ,null=True)
    stud_div=models.CharField(max_length=1, blank=True)
    machine_id = models.CharField(max_length=250, default="N.A", blank=False)
    branch=models.CharField(max_length=250)
    admission_year = models.PositiveIntegerField(
            validators=[MinValueValidator(1900)],null=True, help_text="Use the following format: <YYYY>")
    
    def __str__(self):
        return self.session_id

