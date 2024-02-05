from django.urls import path
from . import views

urlpatterns = [
     path('',views.view_session,name="view_session")
]