from django.urls import path

from proapp import views,adminviews,Nurseviews


urlpatterns = [
     path('admin_home',views.image,name='admin_home'),
     path('',views.home,name='home1'),
     path('login',views.login_view,name='login'),
     path('userform',views.userform,name='userform'),
     path('nurselogin',views.nurselogin,name='nurselogin'),
     path('userlogin',views.userlogin,name='userlogin'),
     path('nurseregister',views.nurse_register,name='nurseregister'),
     path('userregister',views.user_register,name='userregister'),
     path('Add_hospital',adminviews.add_hospital,name='Add_hospital'),
     path('viewnurse',adminviews.view_nurse,name='viewnurse'),
     path('viewuser', adminviews.view_user, name='viewuser'),
     path('viewhospital', adminviews.view_hospital, name='viewhospital'),
     path('add_vaccine',adminviews.add_vaccine,name='add_vaccine'),
     path('viewvaccine',adminviews.view_vaccine,name='viewvaccine'),
     path('nurse_home',Nurseviews.nurse_home,name='nurse_home'),
     path('addcomplaints',Nurseviews.add_complaints,name='addcomplaints'),
     path('viewcomplaints',adminviews.view_complaints,name='viewcomplaints'),

]

