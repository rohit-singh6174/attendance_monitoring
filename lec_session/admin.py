from django.contrib import admin

# Register your models here.
from lec_session.models import Lecture_Session
# Register your models here.

# class Lecture_SessionAdmin(admin.ModelAdmin):
#     list_filter=("subject_name","email","branch","date")
#     list_display=("session_id","subject_name","email","branch","date","start_time","end_time")
   
    
admin.site.register(Lecture_Session)