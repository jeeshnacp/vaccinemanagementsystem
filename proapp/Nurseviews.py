from django.contrib import messages
from django.shortcuts import redirect, render

from proapp.forms import complaintform, scheduleform
from proapp.models import vaccine, User, hospital, schedule, complaints


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
    data=User.objects.all()
    return render(request,'Nurse_View_User.html',{'data':data})

def nurse_view_hospital(request):
    data=hospital.objects.all()
    return render(request,'Nurse_View_Hospital.html',{'data':data})

def nurse_add_schedule(request):
    form = scheduleform()
    if request.method == 'POST':
        form = scheduleform(request.POST)
        print('hi')
        if form.is_valid():
            print('hello')
            form.save()
            messages.info(request, 'successfully added')
            return redirect('nurse_home')
    return render(request, 'Nurse_Add_Schedule.html', {'form': form})

def nurse_view_schedule(request):
    data=schedule.objects.all()
    return render(request,'Nurse_View_Schedule.html',{'data':data})

def update_schedule(request,id):
    n=schedule.objects.get(id=id)
    if request.method=='POST':
        form=scheduleform(request.POST or None,instance=n)
        if form.is_valid():
            form.save()
            return redirect('viewschedule')
    else:
        form=scheduleform(request.POST or None,instance=n)
    return render(request,'Nurse_Add_Schedule.html',{'form':form})

def delete_schedule(request,id=None):
    data =schedule.objects.get(id=id)
    data.delete()
    return redirect('viewschedule')




