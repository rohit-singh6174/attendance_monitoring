from django.shortcuts import render

# Create your views here.
def view_session(request):
    return render(request,"lec_session/view_session.html",{
        "ok":"ok",
    })