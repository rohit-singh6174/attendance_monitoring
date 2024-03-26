from django.urls import path
from . import views

urlpatterns = [
    path('new_attendance/', views.Atten.new_attendance, name='new_attendance'),
    path('view_attendance/',views.Atten.view_attendance, name='view_attendance'),
    path('recent_attendance/',views.Atten.recent_attendance, name="recent_attendance"),
    path('subjectwise_attendanc/',views.Atten.subjectwise_attendanc, name='subjectwise_attendanc'),
    
]