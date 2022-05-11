

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


# Create your views here
from proapp.forms import userregister,loginRegister,nurseregister
from proapp.models import nurse

def image(request):
    return render(request,'admin_temp/index.html')



def home(request):
    return render(request,'homeindex.html')


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
            login(request,user)
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
            user=login_form.save(commit=False)
            user.is_nurse=True
            user.save()
            nurse=nurse_form.save(commit=False)
            nurse.user=user
            nurse.save()
            messages.info(request,'Nurse Registration Successfully')
            return redirect('login_view')

    return render(request,'NurseRegistration.html',{'login_form':login_form,'nurse_form':nurse_form})


def user_register(request):
    login_form=loginRegister()
    user_form=userregister()
    if request.method=='POST':
        login_form=loginRegister(request.POST)
        user_form=userregister(request.POST)
        if login_form.is_valid() and user_form.is_valid():
            user=login_form.save(commit=False)
            user.is_user=True
            user.save()
            customer=user_form.save(commit=False)
            customer.user=user
            customer.save()
            messages.info(request,'User Registration Successfully')
            return redirect('login_view')
    return render(request, 'UserRegistration.html', {'login_form': login_form, 'user_form': user_form})

def logout_view(request):
    logout(request)
    return redirect('login_view')