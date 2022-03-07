from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from proapp.filter import HospitalFilter, NurseFilter, UserFilter, VaccineFilter
from proapp.forms import hospitalform, vaccineform, reportcardform, nurseregister
from proapp.models import nurse, customer, hospital, vaccine, complaints, reportcard


def add_hospital(request):
    form = hospitalform()
    if request.method == 'POST':
        form = hospitalform(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'successfully added')
            return redirect('admin_home')
    return render(request, 'admin_temp/add_hospital.html', {'form': form})


def view_nurse(request):
    v = nurse.objects.all()
    nursefilter = NurseFilter(request.GET, queryset=v)
    v = nursefilter.qs
    context = {
        'nurses': v,
        'nursefilter': nursefilter,
    }
    return render(request, 'admin_temp/ViewNurse.html', context)




def view_user(request):
    v = customer.objects.all()
    userfilter = UserFilter(request.GET, queryset=v)
    v = userfilter.qs
    context = {
        'users': v,
        'userfilter': userfilter,
    }
    return render(request, 'admin_temp/ViewUser.html', context)


def view_hospital(request):
    v = hospital.objects.all()
    hospitalfilter = HospitalFilter(request.GET, queryset=v)
    v = hospitalfilter.qs
    context = {
        'hospital': v,
        'hospitalfilter': hospitalfilter,
    }
    return render(request, 'admin_temp/ViewHospital.html', context)


def add_vaccine(request):
    form = vaccineform()
    if request.method == 'POST':
        form = vaccineform(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'successfully added')
            return redirect('admin_home')
    return render(request, 'admin_temp/add_vaccine.html', {'form': form})


def view_vaccine(request):
    v = vaccine.objects.all()
    vaccinefilter = VaccineFilter(request.GET, queryset=v)
    v = vaccinefilter.qs
    context = {
        'vaccine': v,
        'vaccinefilter': vaccinefilter,
    }
    return render(request, 'admin_temp/View_Vaccine.html', context)


def view_complaints(request):
    data = complaints.objects.all()
    return render(request, 'admin_temp/View_complaints.html', {'data': data})




def update_nurse(request, id):
    n = nurse.objects.get(id=id)
    if request.method == 'POST':
        form = nurseregister(request.POST or None, instance=n)
        if form.is_valid():
            form.save()
            return redirect('viewnurse')
    else:
        form = nurseregister(request.POST or None, instance=n)
    return render(request, 'admin_temp/Nurse_update.html', {'form': form})


def delete_nurse(request, id=None):
    data = nurse.objects.get(id=id)
    data.delete()
    return redirect('viewnurse')


def delete_hospital(request, id=None):
    data = hospital.objects.get(id=id)
    data.delete()
    return redirect('viewhospital')


def update_hospital(request, id):
    n = hospital.objects.get(id=id)
    if request.method == 'POST':
        form = hospitalform(request.POST or None, instance=n)
        if form.is_valid():
            form.save()
            return redirect('viewhospital')
    else:
        form = hospitalform(request.POST or None, instance=n)
    return render(request, 'admin_temp/add_hospital.html', {'form': form})


def delete_user(request, id=None):
    data = customer.objects.get(id=id)
    data.delete()
    return redirect('viewuser')


def update_vaccine(request, id):
    n = vaccine.objects.get(id=id)
    if request.method == 'POST':
        form = vaccineform(request.POST or None, instance=n)
        if form.is_valid():
            form.save()
            return redirect('viewvaccine')
    else:
        form = vaccineform(request.POST or None, instance=n)
    return render(request, 'admin_temp/vaccine_update.html', {'form': form})


def delete_vaccine(request, id=None):
    data = vaccine.objects.get(id=id)
    data.delete()
    return redirect('viewvaccine')


def reply_complaint(request, id):
    complaint = complaints.objects.get(id=id)
    if request.method == 'POST':
        r = request.POST.get('reply')
        complaint.reply = r
        complaint.save()
        messages.info(request, 'Reply send for complaint')
        return redirect('viewcomplaints')
    return render(request, 'admin_temp/reply_complaint.html', {'complaint': complaint})
