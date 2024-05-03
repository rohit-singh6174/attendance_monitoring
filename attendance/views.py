from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Machine, Attendance_table
from students.models import Student
from lec_session.models import Lecture_Session
from datetime import datetime
from .filters import AttendanceFilter
from datetime import date
from django.db.models import Q
from collections import defaultdict
import pprint

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
                #1 new current active session 
                session_id = session_data_lst[0]["session_id"]
                session_div= session_data_lst[0]["stud_div"]

                print("Lect Div :",session_div)   
          
                for i in finger_id_list:
                    if Student.objects.filter(year_of_admission=current_admission_year).filter(branch=current_branch).filter(stud_div=session_div).filter(finger_id=i).exists():
                        student_data= list(Student.objects.filter(year_of_admission=current_admission_year).filter(branch=current_branch).filter(finger_id=i).values())
                        student_name=student_data[0]['stud_name']
                        student_roll_no=student_data[0]['stud_roll_no']
                        student_profile= student_data[0]['stud_profile']
                        student_email=student_data[0]['stud_email']
                        student_div=student_data[0]['stud_div']
                        
                        #Check is session is active for that year and branch

                        if Lecture_Session.objects.filter(machine_id=machine_id).filter(is_active=True): 
                            print(f'{student_name}:{student_roll_no}:{student_email}:{student_profile}')
                #           
                            if Attendance_table.objects.filter(roll_no=student_roll_no, admission_year=current_admission_year, session_id=session_id, is_present=True).exists():
                                msg="Session : ",str(session_id)," Attendance Marked Already for  Rollno :",str(student_roll_no)
                                return HttpResponse(msg)
                            
                            attendance_obj= Attendance_table.objects.create(stud_name=student_name,roll_no=student_roll_no,sem_type=True,session_id=session_id,is_present=True,date=datetime.now().date(),branch=current_branch,admission_year=current_admission_year,stud_profile=student_profile,stud_email=student_email,stud_div=student_div)
                            attendance_obj.save()

                        else:
                            return HttpResponse(f"No session is active for --> {current_admission_year}")                        
                    else:
                        return HttpResponse("Student Doesn't Exist")
                    
                return HttpResponse("OK")
            else:
                return HttpResponse("This Machine is Not Registered")
            
        
        

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

        if request.user.is_authenticated:
            email = request.user.email
            current_date = date.today()


        
            active_session = Lecture_Session.objects.filter(email=email, is_active=True, date=current_date).first()
            print(active_session)
            if active_session:
                attendance_data = Attendance_table.objects.filter(session_id=active_session.session_id)
                print(attendance_data)

                
                context = {
                    "attendance": attendance_data,
                    "recent_session":active_session,
                   
                }
                return render(request, "attendance/recent_attendance.html", context)
            else:
                 return render(request, "attendance/recent_attendance.html")
            # if active_session:
            #     attendance_data = Attendance_table.objects.filter(session_id=active_session.session_id)
            #     context = {
            #         "attendance": attendance_data,
            #         }
            #     return render(request, "attendance/recent_attendance.html", context)
            # else:
            #     return render(request,"attendance/recent_attendance.html")
            # return HttpResponse("OK")

            
            
                                                              
    

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

    def subjectwise_attendanc(request):

        all_attendance=Attendance_table.objects.all()
        students= Student.objects.all()

        allsession_lst=Lecture_Session.objects.filter(email=request.user.email).values("session_id","date","subject_name").order_by('-session_id')

        session_lst= Lecture_Session.objects.filter(email=request.user.email).values("session_id","date","subject_name").order_by('-session_id')


        if request.method == 'POST':
            admission_year = request.POST.get('admission_year')
            branch=request.POST.get('branch')
            sem=request.POST.get('sem')
            div=request.POST.get('div')
            subject=request.POST.get('subject')

            if sem =='Both':
                session_lst = Lecture_Session.objects.filter(email=request.user.email, admission_year=admission_year).filter(branch=branch).filter(stud_div=div).filter(subject_name=subject).values("session_id", "date", "subject_name").order_by('-session_id')
        

            session_lst = Lecture_Session.objects.filter(email=request.user.email, admission_year=admission_year).filter(branch=branch).filter(sem_type=sem).filter(stud_div=div).filter(subject_name=subject).values("session_id", "date", "subject_name").order_by('-session_id')

            pprint.pp(session_lst)

        attendance_dict = defaultdict(dict)

        for session in session_lst:
            session_id = session['session_id']
            attendance_records = Attendance_table.objects.filter(session_id=session_id)
            for attendance in attendance_records:
                student_roll_no = attendance.roll_no
                is_present = attendance.is_present
                attendance_dict[student_roll_no][session_id] = is_present
             
        # pprint.pp(attendance_dict)

         # Calculate total attendance for each student
        for student in students:
            total_attendance = sum(1 for session_attendance in attendance_dict[student.stud_roll_no].values() if session_attendance)
            student.total_attendance = total_attendance
        
         
        context ={
        "attendance":all_attendance,
        'session_id_lst':session_lst,
        "students":students,
        "attendance_dict":attendance_dict
        }
        
        return render(request,'attendance/subjectwise_attendanc.html',context)

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


            