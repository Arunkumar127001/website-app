from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('',views.home,name='Home'),
    path('about/',views.about,name='About'),
    path('admission/',views.admission,name='Admission'),
    # path('about',views.about,name='About'),
    path('contact/',views.contact,name='Contact'),
    path('signup/',views.signup,name='Signup'),
    path('home/',views.home,name='Home'),
    path('students/',views.students,name='Students'),
    

    
]
