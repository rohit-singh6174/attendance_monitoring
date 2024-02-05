from django.urls import path
from . import views

urlpatterns = [
    path('new_attendance/', views.Atten.new_attendance, name='new_attendance'),

]