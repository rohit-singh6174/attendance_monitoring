from django.shortcuts import render, HttpResponse
from lec_session.forms import Create_session
from lec_session.models import Lecture_Session
from django.contrib import messages, auth
from attendance.models import Machine
from datetime import datetime
import random


def get_session_id():
    current_datetime = datetime.now()
    # Format a specific date and time
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    formatted_datetime=formatted_datetime.replace("-","")
    formatted_datetime=formatted_datetime.replace(":","")
    rd = str(random.randint(1000,9999))
    formatted_datetime=(formatted_datetime+rd).replace(" ","")
    return formatted_datetime

# Create your views here.
def view_session(request):
    
    sessions = Lecture_Session.objects.filter(email=request.user.email).order_by('-session_id')[0:50]
    context ={
        "sessions":sessions
    }

    return render(request,"lec_session/view_session.html", context)


def create_session(request):
    if request.user.is_authenticated:
        form=Create_session(request.POST)
        if request.method == 'POST':
            if form.is_valid():
                email=request.user.email
                year_of_admission = form.cleaned_data['year_of_admission']
                subject_name=form.cleaned_data['subject_name']
                stud_div=form.cleaned_data['stud_div']
                branch=form.cleaned_data['branch']
                machine_data=list(Machine.objects.filter(admission_year=year_of_admission, branch=branch).values())
                machine_id=machine_data[0]['machine_id']
                if Lecture_Session.objects.filter(machine_id=machine_id).order_by('date').filter(is_active=True).exists():
                    return HttpResponse('Session is already started')
                else:
                    session_id=get_session_id()
                    new_session=Lecture_Session.objects.create(session_id=session_id,is_active=True,subject_name=subject_name,email=email,start_time=datetime.now().time(),date=datetime.now().date(),stud_div=stud_div,machine_id=machine_id,branch=branch)
                    new_session.save()
                    messages.success(request, 'Session Create Succssfully')
            else:
                print("Form Failed")
            
        else:
            form=Create_session(request.POST)
            pass
        
        context={
        "form":form
        }

    return render(request,"lec_session/create_session.html",context)





def test_session(request):
    if request.method == 'POST':
        form=Create_session(request.POST)
        if form.is_valid():
            print("ok")
            email=request.user.email
            year_of_admission = form.cleaned_data['year_of_admission']
            subject_name=form.cleaned_data['subject_name']
            stud_div=form.cleaned_data['stud_div']
            branch=form.cleaned_data['branch']

            machine_data=list(Machine.objects.filter(admission_year=year_of_admission, branch=branch).values())
            machine_id=machine_data[0]['machine_id']
            if Lecture_Session.objects.filter(machine_id=machine_id).order_by('date').filter(is_active=True).exists():
                return HttpResponse('Session is already started')
            else:
                session_id=get_session_id()
                new_session=Lecture_Session.objects.create(session_id=session_id,is_active=True,subject_name=subject_name,email=email,start_time=datetime.now().time(),date=datetime.now().date(),stud_div=stud_div,machine_id=machine_id,branch=branch)
                new_session.save()
                messages.success(request, 'Session Create Succssfully')
        else:
            print("Failed")
    
    else:
        form=Create_session(request.POST)

    context={
        "form":form
    }
    return render(request,'lec_session/testform.html',context)



# def create_session(request):
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             # print("ok")
#             admission_year = request.POST.get('admission_year')
#             branch=request.POST.get('branch')
#             div=request.POST.get('div')
#             subject_name=request.POST.get('subject_name')
#             email=request.user.email


#             machine_data=list(Machine.objects.filter(admission_year=admission_year, branch=branch).values())
#             machine_id=machine_data[0]['machine_id']
#             if Lecture_Session.objects.filter(machine_id=machine_id).order_by('date').filter(is_active=True).exists():
#                 return HttpResponse('Session is already started')
#             else:
#                 session_id=get_session_id()
#                 new_session=Lecture_Session.objects.create(session_id=session_id,is_active=True,subject_name=subject_name,email=request.user.email,start_time=datetime.now().time(),date=datetime.now().date(),stud_div=div,machine_id=machine_id,branch=branch)
#                 new_session.save()
#                 messages.success(request, 'Session Create Succssfully')

#         else:
#             pass

#     return render(request,"lec_session/create_session.html")

