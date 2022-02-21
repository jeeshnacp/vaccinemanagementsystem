import profile

from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from proapp.models import User, schedule, appointment


def user_home(request):
    return render(request,'User_home.html')

def user_profile(request):
    user = request.user
    profile =User.objects.filter(user=user)
    return render(request,'user_profile.html',{'profile':profile})

def user_view_schedule(request):
    data=schedule.objects.all()
    return render(request,'User_View_Schedule.html',{'data':data})


def schedule_user(request):
    s=schedule.objects.all()

    return render(request,'User_View_Schedule.html',{'s':s})


def take_appointment(request,id):
    schedules=schedule.objects.get(id=id)
    u=User.objects.get(user=request.user)
    appointments=appointment.objects.filter(user=u,schedules=schedules)
    if appointments.exists():
        messages.info(request,'you have already requested appointment for this schedule')
        return redirect('userschedule')
    if request.method=='POST':
            obj=appointment()
            obj.user=u
            obj.schedules=schedules
            obj.save()
            messages.info(request,'appointment booked successfully')
            return redirect('appointments')
    return render(request,'take_appointmnet.html',{'schedules:schedules'})

def view_appoint(request):
    u=User.objects.get(user=request.user)
    a=appointment.objects.filter(user=u)
    return render(request,'userview_appointment.html',{'a':a})
