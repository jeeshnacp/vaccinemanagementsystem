import profile

from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from proapp.forms import complaintform
from proapp.models import customer, Schedule, appointment, reportcard


def user_home(request):
    return render(request, 'user_temp/User_home.html')


def user_profile(request):
    profile = customer.objects.filter(user=request.user)
    return render(request, 'user_temp/user_profile.html', {'profile': profile})


def user_view_schedule(request):
    data = Schedule.objects.all()
    return render(request, 'user_temp/User_View_Schedule.html', {'data': data})


def schedule_user(request):
    s = Schedule.objects.all()

    return render(request, 'user_temp/User_View_Schedule.html', {'s': s})


def take_appointment(request, id):
    schedule = Schedule.objects.get(id=id)
    u = customer.objects.get(user=request.user)
    appointments = appointment.objects.filter(user=u,schedule=schedule)
    if appointments.exists():
        messages.info(request, 'you have already requested appointment for this schedule')
        return redirect('userviewappointment')
    else:
        if request.method == 'POST':
            obj = appointment()
            obj.user = u
            obj.schedule = schedule
            obj.save()
            messages.info(request, 'appointment booked successfully')
            return redirect('userviewappointment')
    return render(request, 'user_temp/take_appointment.html', {'schedules': schedule})


def view_appoint(request):
    u = customer.objects.get(user=request.user)
    a = appointment.objects.filter(user=u)
    return render(request, 'user_temp/userview_appointment.html', {'appointment': a})


def user_report(request):
    u = customer.objects.get(user=request.user)
    data = reportcard.objects.filter(patient=u)
    context = {
        'data': data
    }
    return render(request, 'user_temp/User_View_reportcard.html',context)

def add_complaint(request):
    if request.method == 'POST':
        form = complaintform(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'successfully added')
            return redirect('user_home')
    else:
        form = complaintform()
    return render(request, 'user_temp/add_complaints.html', {'form': form})

