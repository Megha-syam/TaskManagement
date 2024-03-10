from django.urls import path,include
from .views import *

urlpatterns=[
    path('',main,name="main"),
    path('login', login, name="login"),
    path('register', register, name="register"),
    path('contactus',contactus,name="contactus"),
    path('aboutus',aboutus,name="aboutus"),
    path('dashboard.html',home,name="dashboard" ),

    path('calendar.html',calendar,name="calendar"),

    path('task.html',taskviewer,name="task"),
    path('vtask.html',vtask,name="view"),

    path('sdetails',sdetails,name="sdetails"),

    path('get_tasks', get_tasks, name='get_tasks'),

    path('calendar', calendar_view, name='calendar'),




]