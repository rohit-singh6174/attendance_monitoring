from django.urls import path
from . import views
urlpatterns = [
    path('',views.student_list, name="students_list"),
    path('enroll_student/',views.enroll_student, name="enroll_student"),
    path('student_profile/<str:stud_roll_no>/',views.student_profile, name='student_profile'),
]
