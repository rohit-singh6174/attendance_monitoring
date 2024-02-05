from django.contrib import admin

from .models import Machine, Attendance_table
# Register your models here.

class MachineAdmin(admin.ModelAdmin):
    list_filter=("branch","admission_year")
    list_display=("machine_id","branch","admission_year")
   
    
admin.site.register(Machine,MachineAdmin)
admin.site.register(Attendance_table)