from django.contrib import admin

from .models import Machine, Attendance_table
# Register your models here.

class MachineAdmin(admin.ModelAdmin):
    list_filter=("branch","admission_year")
    list_display=("machine_id","branch","admission_year")

class AttendanceAdmin(admin.ModelAdmin):
    list_filter=("session_id","admission_year","branch","roll_no")
    
admin.site.register(Machine,MachineAdmin)
admin.site.register(Attendance_table,AttendanceAdmin)