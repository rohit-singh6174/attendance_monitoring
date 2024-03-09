import django_filters
from django import forms
from .models import Attendance_table
from django_filters import DateFilter

from datetime import datetime

class DateInput(forms.DateInput):
    input_type='date'


class AttendanceFilter(django_filters.FilterSet):

    class Meta:
        model = Attendance_table
        fields= '__all__'
        exclude=['id','stud_name','roll_no','session_id']
        widgets={'date': DateInput()}
    
   
       
       