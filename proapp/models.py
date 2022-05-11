from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Login(AbstractUser):
    is_nurse = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)


class hospital(models.Model):
    Hospital_Name = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.Hospital_Name


class nurse(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE,related_name='nurse')
    Nurse_Name = models.CharField(max_length=20)
    Contact_no = models.CharField(max_length=50)
    Address = models.TextField()
    Email = models.EmailField()
    Hospital_name = models.ForeignKey(hospital, on_delete=models.CASCADE)

    def __str__(self):
        return self.Nurse_Name


class customer(models.Model):
    user = models.OneToOneField(Login, on_delete=models.CASCADE,related_name='customer')
    Name = models.CharField(max_length=20)
    contact_no = models.IntegerField()
    Address = models.TextField()
    child_name = models.CharField(max_length=20)
    child_age = models.IntegerField()
    child_gender = models.CharField(max_length=20)
    recent_vaccinations = models.TextField()

    def __str__(self):
        return self.Name


class vaccine(models.Model):
    vaccine_name = models.CharField(max_length=50)
    vaccine_type = models.CharField(max_length=50)
    description = models.TextField()
    approvel_status = models.IntegerField(default=0)

    def __str__(self):
        return self.vaccine_name


class reportcard(models.Model):
    vaccine = models.ForeignKey(vaccine, on_delete=models.DO_NOTHING)
    patient = models.ForeignKey(customer, on_delete=models.DO_NOTHING)


class Schedule(models.Model):
    Hospital = models.ForeignKey(hospital, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()


class appointment(models.Model):
    user = models.ForeignKey(customer, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    vaccine_name = models.CharField(max_length=20)
    vaccinated = models.CharField(max_length=20)
    status = models.BooleanField(default=False)


class complaints(models.Model):
    user = models.ForeignKey(customer, on_delete=models.CASCADE)

    subject = models.CharField(max_length=50)
    complaint = models.CharField(max_length=50)
    date = models.DateField()
    reply = models.CharField(max_length=50)
