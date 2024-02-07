from django.shortcuts import render,redirect,get_object_or_404
from .models import Student
from .forms import EnrollStudentForm, EditStudentForm
from django.contrib import messages, auth


# Create your views here.
def student_list(request):
    students = Student.objects.all()
    context ={
        "students":students
    }
    return render(request,'student_list.html', context)


def enroll_student(request):
    if request.method == 'POST':
        form = EnrollStudentForm(request.POST, request.FILES)
        if form.is_valid():
            stud_roll_no = form.cleaned_data['stud_roll_no']
            stud_email = form.cleaned_data['stud_email']
            if Student.objects.filter(stud_roll_no=stud_roll_no,stud_email=stud_email).exists():
                messages.error(request, 'Student Already Enrolled')

            else:
             stud_name = form.cleaned_data['stud_name']
             stud_phone=form.cleaned_data['stud_phone']
             year_of_admission=form.cleaned_data['year_of_admission']
             stud_div=form.cleaned_data['stud_div']
             branch=form.cleaned_data['branch']
             finger_id=form.cleaned_data['finger_id']
             stud_profile=form.cleaned_data['stud_profile']

             
             enrolled= Student(stud_roll_no=stud_roll_no,stud_name=stud_name,stud_phone=stud_phone,stud_email=stud_email,stud_div=stud_div,branch=branch,stud_profile=stud_profile,finger_id=finger_id,year_of_admission=year_of_admission)
             enrolled.save()
             messages.success(request, 'Student Enrolled Successfully')
        else:
            # print("Not Valid")
            messages.error(request, 'Failed Student Enrolled')
    else:
        form = EnrollStudentForm(request.POST)
        
    
    context={
        "form":form
    }
    
    return render(request,'enroll_student.html',context)


def student_profile(request, stud_roll_no):
    student = get_object_or_404(Student, stud_roll_no=stud_roll_no)

    if request.method == 'GET':
        context={
            "student":student
            }
        return render(request, 'student_profile.html',context)
    

    
    # current_student = Student.objects.get(stud_roll_no=stud_roll_no)
    # if request.method == 'GET':
      
    #     context = {
    #         'form': EditStudentForm(instance=stud),
    #         'stud_roll_no':stud_roll_no
    #         }
    #     return render(request, 'student_profile.html', context)
    
    # elif request.method == 'POST':
    #     form = EditStudentForm(request.POST,request.FILES,instance=stud)
    #     if form.is_valid():
    #         print("OK Valid")
    #     else:
    #         print("Not Valid")
        
    #     return render(request,'student_profile.html')


    #     form = EditStudentForm(request.POST or None, instance=current_student)

    #     if request.method == 'POST':
    #         if form.is_valid():
    #             form.save()
    #             messages.success(request, 'Student profile updated successfully')
    #             return redirect('students_list')  # Replace with the correct URL name

    # else:
    #     messages.error(request, 'Student Does not Exist')
    #     return redirect('students_list')  # Replace with the correct URL name

