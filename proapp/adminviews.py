from django.contrib import messages
from django.shortcuts import redirect, render

from proapp.forms import hospitalform


def add_hospital(request):
    form=hospitalform()
    if request.method=='POST':
        form=hospitalform(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,'successfully added')
            return redirect('admin_home')
    return render(request,'add_hospital.html',{'form':form})
