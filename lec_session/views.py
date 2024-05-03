from django.shortcuts import render, HttpResponse, redirect
from lec_session.forms import Create_session
from lec_session.models import Lecture_Session
from django.contrib import messages, auth
from attendance.models import Machine
from datetime import datetime
from  attendance.models import Attendance_table
from students.models import Student
import random
from zoneinfo import ZoneInfo


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
                sem_input = request.POST.get('sem_type')
                sem_type=False

                if sem_input =='None':
                    sem_type= False
                elif sem_input =='on':
                    sem_type=True

                print(sem_type)


                machine_data=list(Machine.objects.filter(admission_year=year_of_admission, branch=branch).values())
                machine_id=machine_data[0]['machine_id']
                if Lecture_Session.objects.filter(machine_id=machine_id).order_by('date').filter(is_active=True).exists():
                    return HttpResponse('Session is already started')
                else:
                    session_id=get_session_id()
                    new_session=Lecture_Session.objects.create(session_id=session_id,admission_year=year_of_admission,is_active=True,subject_name=subject_name,email=email,start_time=datetime.now().time(),date=datetime.now().date(),stud_div=stud_div,machine_id=machine_id,branch=branch, sem_type=sem_type)
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

def end_session(request,session_id):
   if request.user.is_authenticated:
        
        # Retrieve the Lecture_Session object based on the session_id
        print("Session ID:",session_id)
        lecture_session = Lecture_Session.objects.get(session_id=session_id)

        present_students = Attendance_table.objects.filter(session_id=session_id,is_present=True,stud_div=lecture_session.stud_div).values_list("roll_no", flat=True)
        
        # Get the absent students based on their roll numbers
        
        # absent_students = Student.objects.exclude(stud_roll_no__in=present_students,stud_div=lecture_session).values("stud_roll_no", "stud_name")
        
        absent_students = Student.objects.filter(
            year_of_admission=lecture_session.admission_year,
            branch=lecture_session.branch,
            stud_div=lecture_session.stud_div
        ).exclude(
            stud_roll_no__in=present_students
        ).values("stud_roll_no", "stud_name")

        
         # Retrieve the details of absent students
       
        student_lst = Student.objects.filter(stud_roll_no__in=[student['stud_roll_no'] for student in absent_students]).values("stud_roll_no", "stud_name","branch","year_of_admission","stud_profile","stud_email")
        # print("Student list :", student_lst)

        date = str(datetime.now(tz=ZoneInfo('Asia/Kolkata')).strftime("%Y-%m-%d"))

        try:
            teacher_email= request.user.email
            print(teacher_email)
            time = str(datetime.now(tz=ZoneInfo('Asia/Kolkata')).strftime("%H:%M:%S"))
            Lecture_Session.objects.filter(email=teacher_email).filter(is_active=True).update(is_active=False,end_time=time)
            
            for student in student_lst:
                Attendance_table.objects.create(date=date, roll_no=student["stud_roll_no"], session_id=session_id, stud_name=student["stud_name"], branch=student["branch"], admission_year=student["year_of_admission"],stud_profile=student["stud_profile"],stud_email=student["stud_email"])

            # return HttpResponse("Session ID: " +session_id + " ended successfully")
            messages.success(request,"Session ID: " +session_id + " ended successfully")
            return redirect('view_session')

        except:
            messages.danger(request,"Session Faield to ended")
            return redirect('view_session')

        
def session_summary(request,session_id):
   if request.user.is_authenticated:
       print(session_id)

       current_session = Lecture_Session.objects.filter(session_id=session_id).first()

       session_attendance= Attendance_table.objects.filter(session_id=current_session.session_id).all()

       total_attendance_count = session_attendance.count()
       present=session_attendance.filter(is_present=True).count()
       absent=session_attendance.filter(is_present=False).count()
       


       context={
           "sessions":current_session,
            "attendances":session_attendance,
            "total_attendance_count":total_attendance_count,
            "present":present,
            "absent":absent
       }
       return render(request,"lec_session/session_summary.html",context)
    

# def test_session(request):
#     if request.method == 'POST':
#         form=Create_session(request.POST)
#         if form.is_valid():
#             print("ok")
#             email=request.user.email
#             year_of_admission = form.cleaned_data['year_of_admission']
#             subject_name=form.cleaned_data['subject_name']
#             stud_div=form.cleaned_data['stud_div']
#             branch=form.cleaned_data['branch']

#             machine_data=list(Machine.objects.filter(admission_year=year_of_admission, branch=branch).values())
#             machine_id=machine_data[0]['machine_id']
#             if Lecture_Session.objects.filter(machine_id=machine_id).order_by('date').filter(is_active=True).exists():
#                 return HttpResponse('Session is already started')
#             else:
#                 session_id=get_session_id()
#                 new_session=Lecture_Session.objects.create(session_id=session_id,is_active=True,subject_name=subject_name,email=email,start_time=datetime.now().time(),date=datetime.now().date(),stud_div=stud_div,machine_id=machine_id,branch=branch)
#                 new_session.save()
#                 messages.success(request, 'Session Create Succssfully')
#         else:
#             print("Failed")
    
#     else:
#         form=Create_session(request.POST)

#     context={
#         "form":form
#     }
#     return render(request,'lec_session/testform.html',context)



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

