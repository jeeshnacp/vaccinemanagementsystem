import profile

from django.shortcuts import render

from proapp.models import User


def user_home(request):
    return render(request,'User_home.html')


# def user_profile(request):
#     u = request.user
#     profile =User.objects.filter(user=u)
#     return render(request,'users-profile.html',{'profile':profile})