import re

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from proapp.models import Login,nurse, hospital, User, vaccine, complaints, schedule, reportcard



def phone_number_validator(value):
    if not re.compile(r'^[7-9]\d{9}$').match(value):
        raise ValidationError('This is not valid number')


class loginRegister(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput)

    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2',)

#
class nurseregister(forms.ModelForm):
    Contact_no=forms.CharField(validators=[phone_number_validator])
    class Meta:
        model = nurse
        fields = ('Nurse_Name', 'Contact_no', 'Address', 'Email','Hospital_name')

class hospitalform(forms.ModelForm):
    contact_no = forms.CharField(validators=[phone_number_validator])
    class Meta:
        model= hospital
        fields=('Hospital_Name','place','contact_no','email')


class userregister(forms.ModelForm):
    class Meta:
        model= User
        fields=('Name','contact_no','Address','child_name','child_age','child_gender')

class vaccineform(forms.ModelForm):
    class Meta:
        model= vaccine
        fields=('vaccine_name','vaccine_type','description')

class complaintform(forms.ModelForm):
    class Meta:
        model=complaints
        fields=('subject','complaint','date')

class scheduleform(forms.ModelForm):
    class Meta:
        model=schedule
        fields=('Hospital','date','start_time','end_time')

class reportcardform(forms.ModelForm):
    class Meta:
        model=reportcard
        fields=('vaccine','patient')
