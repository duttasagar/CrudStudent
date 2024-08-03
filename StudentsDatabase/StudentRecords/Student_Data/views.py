from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

def add_show(request):
    if request.method == 'POST':
        tt = StudentRegistration(request.POST)
        if tt.is_valid():
            nm = request.POST['name']
            em = request.POST['email']
            pm = request.POST['password']
            AM = User(name = nm , email = em , password = pm)
            AM.save()
            return HttpResponseRedirect("/")
        else:
            tt = StudentRegistration()
        return render(request , 'addandshow.html' )
    else:
        FM = StudentRegistration()
    dt = User.objects.all()
    return render(request , 'addandshow.html' , {'form' : FM , 'stu': dt})


def delete_data(request , id):
     if request.method == 'POST':
        dt = User.objects.get(pk=id)
        dt.delete()
        return HttpResponseRedirect("/")
# Create your views here.

def update_data(request , id):
    if request.method == 'POST':
        PI = User.objects.get(pk = id)
        AM = StudentRegistration(request.POST , instance=PI)
        AM.save()
        return HttpResponseRedirect("/")
    else:
        PI = User.objects.get(pk = id)
        AM = StudentRegistration( instance=PI)
        return render(request , "updatestudent.html" ,{'formss' : AM})













