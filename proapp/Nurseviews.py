from django.contrib import messages
from django.shortcuts import redirect, render

from proapp.forms import complaintform


def nurse_home(request):
    return render(request, 'Nurse_home.html')


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
