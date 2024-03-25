from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from alertapp.forms import AlertLoginForm


def alertlogin(request):
    
    if request.method == "POST":
        form = AlertLoginForm(request.POST)  # Bind the form with POST data
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            if email == "rohit224455@gmail.com":
                print("ok")
                return JsonResponse({'status': 'success', 'message': 'Login successful'})
            else:
                print("not ok")
                return JsonResponse({'status': 'error', 'message': 'Login failed'})
        else:
            # Form is not valid
            return JsonResponse({'status': 'error', 'message': 'Form data is not valid'})
    
    form = AlertLoginForm(request.POST)
    context={
        "form":form
    }
    return render(request, "alertapp/alertlogin.html",context)

def homealert(request):
    return render(request, "alertapp/alerthome.html")
