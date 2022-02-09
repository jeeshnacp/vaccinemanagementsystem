from django.contrib import messages
from django.shortcuts import redirect, render

from proapp.forms import complaintform, scheduleform
from proapp.models import vaccine, user, hospital


def nurse_home(request):
    return render(request,'Nurse_home.html')


def add_complaints(request):
    if request.method == 'POST':
        form = complaintform(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'successfully added')
            return redirect('nurse_home')
    else:
        form = complaintform()
    return render(request, 'add_complaints.html', {'form': form})

def nurse_view_vaccine(request):
    data=vaccine.objects.all()
    return render(request,'Nurse_View_Vaccine.html',{'data':data})
def nurse_view_user(request):
    data=user.objects.all()
    return render(request,'Nurse_View_User.html',{'data':data})

def nurse_view_hospital(request):
    data=hospital.objects.all()
    return render(request,'Nurse_View_Hospital.html',{'data':data})

def nurse_add_schedule(request):
    if request.method == 'POST':
        form = scheduleform(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'successfully added')
            return redirect('nurse_home')
    else:
        form = scheduleform()
    return render(request, 'Nurse_Add_Schedule.html', {'form': form})



