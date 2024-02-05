from django.contrib import admin
from .models import Department, Student
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_filter=("branch","stud_div","year_of_admission")
    list_display=("stud_roll_no","stud_name","stud_email","branch","finger_id")
   
    

admin.site.register(Department)
admin.site.register(Student,StudentAdmin)