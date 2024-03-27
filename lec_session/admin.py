from django.contrib import admin

# Register your models here.
from lec_session.models import Lecture_Session
# Register your models here.

class Lecture_SessionAdmin(admin.ModelAdmin):
    list_filter=("subject_name","is_active","branch","date")
    list_display=("session_id","subject_name","branch","date","is_active","admission_year")
   
    
admin.site.register(Lecture_Session,Lecture_SessionAdmin)