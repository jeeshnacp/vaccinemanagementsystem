import profile

from django.shortcuts import render

from proapp.models import User, schedule


def user_home(request):
    return render(request,'User_home.html')


def user_profile(request):
    user = request.user
    profile =User.objects.filter(user=user)
    return render(request,'user_profile.html',{'profile':profile})

def user_view_schedule(request):
    data=schedule.objects.all()
    return render(request,'User_View_Schedule.html',{'data':data})
