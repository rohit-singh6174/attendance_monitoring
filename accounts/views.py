from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from .models import Account
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth import logout
from django.http import JsonResponse


# Create your views here.
class Register(View):
    def get(self,request):
        form = RegistrationForm(request.POST)
        context={
            "form":form
        }
        return render(request,"accounts/register.html",context)
     
    def post(self,request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            if Account.objects.filter(phone_number=phone_number).exists():
                messages.error(request,'Phone Number Already Exist')
            else:
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                phone_number = form.cleaned_data['phone_number']
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                username = email.split("@")[0]

                user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
                user.save()
                messages.success(request,'Registration Successful')
                return redirect('register')
        else:
            messages.error(request,'Registration Failed')
        context={
            "form":form
        }
        return render(request,"accounts/register.html",context)

class Login(View):
    def get(self, request):
        form = LoginForm()  # Create an instance of the form
        context = {
            "form": form
            }
        return render(request, "accounts/login.html", context)
    
    def post(self,request):
        form = LoginForm(request.POST)

        if form.is_valid():
            #print("Ok")
            email = form.cleaned_data['email']
            if Account.objects.filter(email=email).exists():
                password= form.cleaned_data['password']
                user  =auth.authenticate(email=email,password=password)
                if user is not None:
                    print("Ok")
                    auth.login(request, user)
                    messages.success(request, 'You are logged in')
                    return redirect('home')
                else:
                    print("Invalid Password")
            else:
                print("Email Does not Exist")


        context={
            "form":form
        }
        return render(request,"accounts/login.html",context)
        
    # def post(self,request):
    #     form = LoginForm(request.POST)

    #     if form.is_valid():
    #         #print("Ok")
    #         email = form.cleaned_data['email']
    #         if Account.objects.filter(email=email).exists():
    #             password= form.cleaned_data['password']
    #             user  =auth.authenticate(email=email,password=password)
    #             if user is not None:
    #                 print("Ok")
    #                 auth.login(request, user)
    #                 messages.success(request, 'You are logged in')
    #                 return redirect('home')
    #             else:
    #                 print("Invalid Password")
    #         else:
    #             print("Email Does not Exist")


    #     context={
    #         "form":form
    #     }
    #     return render(request,"accounts/login.html",context)



# @method_decorator(login_required(login_url='login'), name='dispatch')
class Logout(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        print("logout")
        return redirect('login')
    

# def  register(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         # print("Button OK")
#         if form.is_valid():
#             phone_number = form.cleaned_data['phone_number']
#             if Account.objects.filter(phone_number=phone_number).exists():
#                 messages.error(request,'Phone Number Already Exist')
#             else:
#                 first_name = form.cleaned_data['first_name']
#                 last_name = form.cleaned_data['last_name']
#                 phone_number = form.cleaned_data['phone_number']
#                 email = form.cleaned_data['email']
#                 password = form.cleaned_data['password']
#                 username = email.split("@")[0]

#                 user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
#                 user.save()
#                 messages.success(request,'Registration Successful')
#                 return redirect('register')
#         else:
#             messages.error(request,'Registration Failed')

#     else:
#         form = RegistrationForm(request.POST)

    
#     context={
#         "form":form
#     }

#     return render(request,"accounts/register.html",context)

# def login(request):

#     return render(request,"accounts/login.html")

