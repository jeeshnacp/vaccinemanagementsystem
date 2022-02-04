from django.contrib import messages
from django.shortcuts import redirect, render

from proapp.forms import hospitalform
from proapp.models import nurse,user,hospital


def add_hospital(request):
    form=hospitalform()
    if request.method=='POST':
        form=hospitalform(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,'successfully added')
            return redirect('admin_home')
    return render(request,'add_hospital.html',{'form':form})


def view_nurse(request):
    data=nurse.objects.all()
    return render(request,'ViewNurse.html',{'data':data})

def view_user(request):
    data=user.objects.all()
    return render(request,'ViewUser.html',{'data':data})

def view_hospital(request):
    data=hospital.objects.all()
    return render(request,'ViewHospital.html',{'data':data})