from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from proapp.forms import hospitalform, vaccineform, reportcardform, nurseregister
from proapp.models import nurse, User, hospital, vaccine, complaints, reportcard

def add_hospital(request):
    form=hospitalform()
    if request.method=='POST':
        form=hospitalform(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,'successfully added')
            return redirect('admin_home')
    return render(request,'admin_temp/add_hospital.html',{'form':form})

def view_nurse(request):
    data=nurse.objects.all()
    return render(request,'admin_temp/ViewNurse.html',{'data':data})

def view_user(request):
    data=User.objects.all()
    return render(request,'admin_temp/ViewUser.html',{'data':data})

def view_hospital(request):
    data=hospital.objects.all()
    return render(request,'admin_temp/ViewHospital.html',{'data':data})

def add_vaccine(request):
    form=vaccineform()
    if request.method=='POST':
        form=vaccineform(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'successfully added')
            return redirect('admin_home')
    return render(request, 'admin_temp/add_vaccine.html', {'form': form})

def view_vaccine(request):
    data=vaccine.objects.all()
    return render(request,'admin_temp/View_Vaccine.html',{'data':data})

def view_complaints(request):
    data=complaints.objects.all()
    return render(request,'admin_temp/View_complaints.html',{'data':data})

def add_reportcard(request):
    form=reportcardform()
    if request.method=='POST':
        form=reportcardform(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,'successfully added')
            return redirect('admin_home')
    return render(request,'admin_temp/add_reportcard.html',{'form':form})

def view_reportcard(request):
    data=reportcard.objects.all()
    return render(request,'admin_temp/View_reportcard.html',{'data':data})

def update_nurse(request,id):
    n=nurse.objects.get(id=id)
    if request.method=='POST':
        form=nurseregister(request.POST or None,instance=n)
        if form.is_valid():
            form.save()
            return redirect('viewnurse')
    else:
        form=nurseregister(request.POST or None,instance=n)
    return render(request,'admin_temp/Nurse_update.html',{'form':form})

def delete_nurse(request,id=None):
    data = nurse.objects.get(id=id)
    data.delete()
    return redirect('viewnurse')

def delete_hospital(request,id=None):
    data = hospital.objects.get(id=id)
    data.delete()
    return redirect('viewhospital')

def update_hospital(request,id):
    n=hospital.objects.get(id=id)
    if request.method=='POST':
        form=hospitalform(request.POST or None,instance=n)
        if form.is_valid():
            form.save()
            return redirect('viewhospital')
    else:
        form=hospitalform(request.POST or None,instance=n)
    return render(request,'admin_temp/add_hospital.html',{'form':form})

def delete_user(request,id=None):
    data =User.objects.get(id=id)
    data.delete()
    return redirect('viewuser')

def update_vaccine(request,id):
    n=vaccine.objects.get(id=id)
    if request.method=='POST':
        form=vaccineform(request.POST or None,instance=n)
        if form.is_valid():
            form.save()
            return redirect('viewvaccine')
    else:
        form=vaccineform(request.POST or None,instance=n)
    return render(request,'admin_temp/vaccine_update.html',{'form':form})


def delete_vaccine(request,id=None):
    data =vaccine.objects.get(id=id)
    data.delete()
    return redirect('viewvaccine')

def reply_complaint(request, id):
    complaint=complaints.objects.get(id=id)
    if request.method=='POST':
        r=request.POST.get('reply')
        complaint.reply=r
        complaint.save()
        messages.info(request,'Reply send for complaint')
        return redirect('view_complaint')
    return render(request,'admin_temp/reply_complaint.html',{'complaint':complaint})




