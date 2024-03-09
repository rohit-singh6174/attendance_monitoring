from django.urls import path
from . import views

urlpatterns = [
     path('',views.view_session,name="view_session"),
     path('create_session/',views.create_session, name="create_session"),
     # path('testform/',views.test_session, name="testform")
]