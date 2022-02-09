from django.shortcuts import render


def user_home(request):
    return render(request,'User_home.html')

def user_profile(request):
    return render(request,'users-profile.html')