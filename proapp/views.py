

from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.shortcuts import render, redirect


# Create your views here
from proapp.forms import nurseregister, loginRegister,userregister
from proapp.models import nurse


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
    login_form=loginRegister()
    nurse_form=nurseregister()
    if request.method=='POST':
        login_form=loginRegister(request.POST)
        nurse_form=nurseregister(request.POST)
        if login_form.is_valid() and nurse_form.is_valid():
            login=login_form.save(commit=False)
            login.is_nurse=True
            login.save()
            nurse=nurse_form.save(commit=False)
            nurse.login=login
            nurse.save()
            messages.info(request,'Nurse Registration Successfully')
            return redirect('login')

    return render(request,'NurseRegistration.html',{'login_form':login_form,'nurse_form':nurse_form})


def user_register(request):
    login_form=loginRegister()
    user_form=userregister()
    if request.method=='POST':
        login_form=loginRegister(request.POST)
        user_form=userregister(request.POST)
        if login_form.is_valid() and user_form.is_valid():
            login=login_form.save(commit=False)
            login.is_user=True
            login.save()
            user=user_form.save(commit=False)
            user.login=login
            user.save()
            messages.info(request,'User Registration Successfully')
            return redirect('login')
    return render(request, 'UserRegistration.html', {'login_form': login_form, 'user_form': user_form})

