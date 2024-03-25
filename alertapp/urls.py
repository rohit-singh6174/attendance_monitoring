from django.urls import path
from . import views

urlpatterns = [
    path('', views.alertlogin, name="alertlogin"),
    path('homealert/', views.homealert, name="homealert")
]
