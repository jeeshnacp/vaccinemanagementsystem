from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
   is_nurse=models.BooleanField(default=False)
   is_user=models.BooleanField(default=False)

class hospital(models.Model):
    Hospital_Name=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    contact_no=models.CharField(max_length=50)
    email=models.EmailField()

    def __str__(self):
        return self.Hospital_Name

class nurse(models.Model):
    Nurse_Name=models.CharField(max_length=20)
    Contact_no=models.CharField(max_length=50)
    Address=models.TextField()
    Email=models.EmailField()
    login=models.ForeignKey(Login,on_delete=models.CASCADE,null=True)
    Hospital_name=models.ForeignKey(hospital,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.Name

class user(models.Model):
    User_Name=models.CharField(max_length=20)
    contact_no = models.IntegerField()
    Address=models.TextField()
    child_name=models.CharField(max_length=20)
    log=models.ForeignKey(Login,on_delete=models.CASCADE)
    child_age=models.IntegerField()
    child_gender=models.CharField(max_length=20)
    recent_vaccinations=models.IntegerField()

    def __str__(self):
        return self.Name

class reportcard(models.Model):
    vaccine=models.CharField(max_length=20)
    patient=models.CharField(max_length=20)

    def __str__(self):
        return self.Name

class schedule(models.Model):
    hospital=models.CharField(max_length=50)
    date=models.DateField()
    start_time=models.TimeField()
    end_time=models.TimeField()

    def __str__(self):
        return self.Name

class vaccine(models.Model):
    vaccine_name=models.CharField(max_length=50)
    vaccine_type=models.CharField(max_length=50)
    description=models.TextField()
    approval_status=models.CharField(max_length=50)

    def __str__(self):
        return self.Name

class appointment(models.Model):
    user=models.CharField(max_length=20)
    schedule=models.DateField()
    vaccine_name=models.CharField(max_length=20)
    vaccinated=models.CharField(max_length=20)
    status=models.CharField(max_length=20)

    def __str__(self):
        return self.Name

class complaints(models.Model):
    users=models.ForeignKey(user,on_delete=models.CASCADE,null=True)
    subject=models.CharField(max_length=50)
    complaint=models.CharField(max_length=50)
    date=models.DateField()
    reply=models.CharField(max_length=50)

