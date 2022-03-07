from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from proapp.filter import NVaccineFilter, NUserFilter, NHospitalFilter
from proapp.forms import complaintform, scheduleform, reportcardform
from proapp.models import vaccine, customer, hospital, schedule, complaints, reportcard


def nurse_home(request):
    return render(request,'nurse_temp/Nurse_home.html')

def add_complaints(request):
    if request.method == 'POST':
        form = complaintform(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'successfully added')
            return redirect('nurse_home')
    else:
        form = complaintform()
    return render(request, 'nurse_temp/add_complaints.html', {'form': form})

def nurse_view_vaccine(request):
    v = vaccine.objects.all()
    nvaccinefilter = NVaccineFilter(request.GET, queryset=v)
    v = nvaccinefilter.qs
    context = {
        'nvaccine': v,
        'nvaccinefilter': nvaccinefilter,
    }
    return render(request, 'nurse_temp/Nurse_View_Vaccine.html', context)


def nurse_view_user(request):
    v = customer.objects.all()
    nuserfilter = NUserFilter(request.GET, queryset=v)
    v = nuserfilter.qs
    context = {
        'nuser': v,
        'nuserfilter': nuserfilter,
    }
    return render(request, 'nurse_temp/Nurse_View_User.html', context)


def nurse_view_hospital(request):
    v =hospital.objects.all()
    nhospitalfilter = NHospitalFilter(request.GET, queryset=v)
    v = nhospitalfilter.qs
    context = {
        'nhospital': v,
        'nhospitalfilter': nhospitalfilter,
    }
    return render(request, 'nurse_temp/Nurse_View_Hospital.html', context)


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
    return render(request, 'nurse_temp/Nurse_Add_Schedule.html', {'form': form})

def nurse_view_schedule(request):
    data=schedule.objects.all()
    return render(request,'nurse_temp/Nurse_View_Schedule.html',{'data':data})

def update_schedule(request,id):
    n=schedule.objects.get(id=id)
    if request.method=='POST':
        form=scheduleform(request.POST or None,instance=n)
        if form.is_valid():
            form.save()
            return redirect('viewschedule')
    else:
        form=scheduleform(request.POST or None,instance=n)
    return render(request,'nurse_temp/Nurse_Add_Schedule.html',{'form':form})

def delete_schedule(request,id=None):
    data =schedule.objects.get(id=id)
    data.delete()
    return redirect('viewschedule')

def add_reportcard(request):
    form = reportcardform()
    if request.method == 'POST':
        form = reportcardform(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'successfully added')
            return redirect('admin_home')
    return render(request, 'nurse_temp/add_reportcard.html', {'form': form})


def view_reportcard(request):
    data = reportcard.objects.all()
    return render(request, 'nurse_temp/View_reportcard.html', {'data': data})

def update_reportcard(request,id):
    n=reportcard.objects.get(id=id)
    if request.method=='POST':
        form=reportcardform(request.POST or None,instance=n)
        if form.is_valid():
            form.save()
            return redirect('viewreportcard')
    else:
        form=reportcardform(request.POST or None,instance=n)
    return render(request,'nurse_temp/add_reportcard.html',{'form':form})

def delete_reportcard(request,id=None):
    data =reportcard.objects.get(id=id)
    data.delete()
    return redirect('viewreportcard')