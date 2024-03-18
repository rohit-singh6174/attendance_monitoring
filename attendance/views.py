from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Machine, Attendance_table
from students.models import Student
from lec_session.models import Lecture_Session
from datetime import datetime
from .filters import AttendanceFilter

from django.views.generic import View
from pyexcel_xlsx import save_data

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
                        student_profile= student_data[0]['stud_profile']
                        student_email=student_data[0]['stud_email']

                        print(f'{student_name}:{student_roll_no}:{student_email}:{student_profile}')
                
                
                        #Check is session is active for that year and branch


                        if Lecture_Session.objects.filter(machine_id=machine_id).filter(is_active=True):
                            
                            attendance_obj= Attendance_table.objects.create(stud_name=student_name,roll_no=student_roll_no,sem_type=True,session_id=session_id,is_present=True,date=datetime.now().date(),branch=current_branch,admission_year=current_admission_year,stud_profile=student_profile,stud_email=student_email)
                            attendance_obj.save()

                        else:
                            return HttpResponse(f"No session is active for --> {current_admission_year}")
                return HttpResponse("OK")
                return HttpResponse("Student Finger Id Not Found")
            return HttpResponse("Finger Id Not Matched")
        

    def view_attendance(request):
        all_attendance=Attendance_table.objects.all()

        session_lst= Lecture_Session.objects.filter(email=request.user.email).values("session_id","date").order_by('-session_id')[0:50]

        if request.user.is_authenticated:
            if request.method == 'POST':
             # Handling POST requests
             date = request.POST.get("selected_date")
             session_id = request.POST.get("session_id")

             print(date)

             if not date and not session_id:
                 all_attendance=Attendance_table.objects.all()

             if date and not session_id:
                 all_attendance = all_attendance.filter(date=date)
             
             if session_id and not date:
                # Display attendance data by session ID
                all_attendance = all_attendance.filter(session_id=session_id)

             if date and session_id:
                # Display attendance data by both date and session ID
                all_attendance = all_attendance.filter(date=date,session_id=session_id)

            
        context ={
        "attendance":all_attendance,
        'session_id_lst':session_lst,
        }
        
        return render(request,'attendance/view_attendance.html',context)
    

    def recent_attendance(request):
        print("ok")
        all_attendance=Attendance_table.objects.all()

        context ={
        "attendance":all_attendance,
        
        }

        return render(request,"attendance/recent_attendance.html",context)
    

    def view_attendance_download(request):
        if request.user.is_authenticated:
           
            if request.method =='GET':
                date = request.GET.get("date")
                session_id = request.GET.get("session_id")

                wb = Workbook()
                ws = wb.active
                title = "Attendance_"+str(date)
                ws.title = title
                response = HttpResponse(content_type='application/ms-excel')
                response['Content-Disposition'] = 'attachment; filename="Attendance.xlsx"'
                headers = ["Name", "roll_no", "session_id","is_present","date"]
                ws.append(headers)

                if(not date=="" or not session_id=="none" or session_id==""):
                    try:
                        if(session_id=="" or session_id =="none"):
                            session_id_lst=Lecture_Session.objects.filter(email=request.user.email).filter(date__gte =  date)
                            attendance_data = Attendance_table.objects.filter(session_id__in =  session_id_lst)
                            for i in attendance_data:
                                ws.append([i.stud_name, i.roll_no, str(i.session_id),str(i.is_present),i.date])

                            # Save the workbook to the HttpResponse
                            wb.save(response)
                            return response
                        else:
                            attendance_data = Attendance_table.objects.filter(session_id =  session_id)
                            for i in attendance_data:
                                ws.append([i.stud_name, i.roll_no, str(i.session_id),str(i.is_present),i.date])

                        # Save the workbook to the HttpResponse
                            wb.save(response)
                            return response
                    except:
                        return HttpResponse('<h3 align="center" , color="red">Failed to view..First View attendance</h3>')
                else:
                    return HttpResponse("<h3 align='center' , color = 'red'>Failed to view.. First View attendance</h3>")
        return redirect("view_attendance")



            # if request.user.is_authenticated:
                # if request.method =='POST':
                #     date = request.POST.get("date")
                #     session_id = request.POST.get("session_id")

                #     if(not date=="" or not session_id=="none" or session_id==""):
                #         try:
                #             if(session_id=="" or session_id =="none"):
                #             session_id_lst=Session.objects.filter(teacher_name=request.user.first_name).filter(date__gte =  date)
                #             attendance_data = Attendance.objects.filter(session_id__in =  session_id_lst)
                #             return JsonResponse({'attendance':list(attendance_data.values())})
                #         else:
                #             attendance_data = Attendance.objects.filter(session_id =  session_id)
                #             return JsonResponse({'attendance':list(attendance_data.values())})
                #     except:
                #         return HttpResponse('0')
                # else:
                #     return HttpResponse("2")
            # else:
        #         session_id_lst=Session.objects.filter(teacher_name=request.user.first_name).values("session_id","date").order_by('-session_id')[0:50]
        #         context={
        #             'session_id_lst':session_id_lst,
        #         }
        #         return render(request,'view_attendance.html',context=context)
        # return redirect("/sign_in")


        



            # res=f"machine: {machine_id}, finger: {fingerprint_id} current machine :{current_machine}"
            # print(current_machine["branch"],current_machine["admission_year"])

            # print(res)


            
            