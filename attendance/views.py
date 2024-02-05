from django.shortcuts import render
from django.http import HttpResponse
from .models import Machine, Attendance_table
from students.models import Student
from lec_session.models import Lecture_Session
from datetime import datetime

# Create your views here.
class Atten:
    def new_attendance(request):
        if request.method =='GET':
            machine_id=request.GET.get("machine_id")
            if Machine.objects.filter(machine_id=machine_id).exists():
                fingerprint_id=request.GET.get("fingerprint_id")
                #finger_id = 1,2,3,8,6  i
                finger_id_list  = fingerprint_id.split(",")
                current_machine=Machine.objects.values('branch', 'admission_year').get(machine_id=machine_id)
                current_branch=current_machine["branch"]
                current_admission_year=current_machine["admission_year"]

                session_data_lst = list(Lecture_Session.objects.filter(machine_id=machine_id).filter(is_active=True).values())
                session_id = session_data_lst[0]["session_id"]   
          
                for i in finger_id_list:
                    if Student.objects.filter(year_of_admission=current_admission_year).filter(branch=current_branch).filter(finger_id=i).exists():
                        student_data= list(Student.objects.filter(year_of_admission=current_admission_year).filter(branch=current_branch).filter(finger_id=i).values())
                        student_name=student_data[0]['stud_name']
                        student_roll_no=student_data[0]['stud_roll_no']
                        print(f'{student_name}:{student_roll_no}')
                        #Check is session is active for that year and branch
                        if Lecture_Session.objects.filter(machine_id=machine_id).filter(is_active=True):
                            attendance_obj= Attendance_table.objects.create(stud_name=student_name,roll_no=student_roll_no,sem_type=True,session_id=session_id,is_present=True,date=datetime.now().date())
                            attendance_obj.save()

                        else:
                            return HttpResponse(f"No session is active for --> {current_admission_year}")

        
                return HttpResponse("OK")
            
                return HttpResponse("Student Finger Id Not Found")


            return HttpResponse("Finger Id Not Matched")
    
                



            # res=f"machine: {machine_id}, finger: {fingerprint_id} current machine :{current_machine}"
            # print(current_machine["branch"],current_machine["admission_year"])

            # print(res)


            
            