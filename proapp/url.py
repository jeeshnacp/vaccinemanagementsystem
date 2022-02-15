from django.urls import path

from proapp import views, adminviews, Nurseviews, Userviews

urlpatterns = [
    path('admin_home', views.image, name='admin_home'),
    path('', views.home, name='home1'),
    path('login', views.login_view, name='login'),
    path('userform', views.userform, name='userform'),
    path('nurselogin', views.nurselogin, name='nurselogin'),
    path('userlogin', views.userlogin, name='userlogin'),
    path('nurseregister', views.nurse_register, name='nurseregister'),
    path('userregister', views.user_register, name='userregister'),
    path('Add_hospital', adminviews.add_hospital, name='Add_hospital'),
    path('viewnurse', adminviews.view_nurse, name='viewnurse'),
    path('viewuser', adminviews.view_user, name='viewuser'),
    path('viewhospital', adminviews.view_hospital, name='viewhospital'),
    path('add_vaccine', adminviews.add_vaccine, name='add_vaccine'),
    path('viewvaccine', adminviews.view_vaccine, name='viewvaccine'),
    path('addreportcard', adminviews.add_reportcard, name='addreportcard'),
    path('viewreportcard', adminviews.view_reportcard, name='viewreportcard'),
    path('updatenurse/<int:id>/',adminviews.update_nurse,name='updatenurse'),
    path('deletenurse/<int:id>/',adminviews.delete_nurse,name='deletenurse'),
    path('updatehospital/<int:id>/',adminviews.update_hospital,name='updatehospital'),
    path('deletehospital/<int:id>/', adminviews.delete_hospital, name='deletehospital'),
    path('deleteuser/<int:id>/',adminviews.delete_user,name='deleteuser'),
    path('updatevaccine/<int:id>/', adminviews.update_vaccine, name='updatevaccine'),
    path('deletevaccine/<int:id>/', adminviews.delete_vaccine, name='deletevaccine'),


    path('nurse_home', Nurseviews.nurse_home, name='nurse_home'),
    path('addcomplaints', Nurseviews.add_complaints, name='addcomplaints'),
    path('viewcomplaints', adminviews.view_complaints, name='viewcomplaints'),
    path('viewvaccines', Nurseviews.nurse_view_vaccine, name='viewvaccines'),
    path('nurseuser', Nurseviews.nurse_view_user, name='nurseuser'),
    path('nursehospital', Nurseviews.nurse_view_hospital, name='nursehospital'),
    path('addschedule', Nurseviews.nurse_add_schedule, name='addschedule'),
    path('viewschedule',Nurseviews.nurse_view_schedule,name='viewschedule'),



    path('user_home', Userviews.user_home, name='user_home'),
    # path('userprofile',Userviews.user_profile,name='userprofile')

]
