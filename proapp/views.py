

from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.shortcuts import render, redirect


# Create your views here
from proapp.forms import nurseregister, loginRegister


def image(request):
    return render(request,'index.html')
def home(request):
    return render(request,'homeindex.html')
def login(request):
    return render(request,'login_index.html')

def userform(request):
    return  render(request,'UserRegistrationindex.html')
def nurselogin(request):
    return  render(request,'Nurselogin_index.html')
def userlogin(request):
    return  render(request,'userlogin_index.html')

def login_view(request):
    if request.method=='POST':
        username=request.POST.get('uname')
        password=request.POST.get('pass')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request)
            if user.is_staff:
               return redirect('admin_home')
            elif user.is_nurse:
                return  redirect('nurse_home')
            elif user.is_user:
                return redirect('user_home')
        else:
            messages.info(request,'invalid credentials')
    return render(request,'login_index.html')

def nurse_register(request):
    user_form=loginRegister()
    nurse_form=nurseregister()
    if request.method=='POST':
        user_form=loginRegister(request.POST)
        nurse_form=nurseregister(request.POST)
        if user_form.is_valid() and nurse_form.is_valid():
            user=user_form.save(commit=False)
            user.is_nurse=True
            user.save()
            nurse=nurse_form.save(commit=False)
            nurse.user=user
            nurse.save()
            messages.info(request,'Nurse Registration Successfully')
            return redirect('login')

    return render(request,'NurseRegistration.html',{'user_form':user_form,'nurse_form':nurse_form})
