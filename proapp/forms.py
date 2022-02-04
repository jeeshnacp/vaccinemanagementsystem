from django import forms
from django.contrib.auth.forms import UserCreationForm

from proapp.models import Login,nurse,hospital,user


class loginRegister(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput)

    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2',)


class nurseregister(forms.ModelForm):
    class Meta:
        model = nurse
        fields = ('Nurse_Name', 'Contact_no', 'Address', 'Email','Hospital_name')

class hospitalform(forms.ModelForm):
    class Meta:
        model= hospital
        fields=('Hospital_Name','place','contact_no','email')


class userregister(forms.ModelForm):
    class Meta:
        model= user
        fields=('Name','contact_no','Address','child_name','child_age','child_gender','recent_vaccinations')
