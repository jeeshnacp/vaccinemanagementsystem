from django.urls import path

from proapp import views,adminviews


urlpatterns = [
     path('admin_home',views.image,name='admin_home'),
     path('',views.home,name='home1'),
     path('login',views.login_view,name='login'),
     path('userform',views.userform,name='userform'),
     path('nurselogin',views.nurselogin,name='nurselogin'),
     path('userlogin',views.userlogin,name='userlogin'),
     path('nurseregister',views.nurse_register,name='nurseregister'),
     path('form',adminviews.add_hospital,name='form')
]
