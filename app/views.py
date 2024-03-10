from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import *



def get_tasks(request):
    date = request.GET.get('date')
    matching_tasks = taskshow.objects.filter(deadline=date)
    tasks_data = [
        {
            'name': task.name,
            'description': task.description,
            'deadline': task.deadline.strftime('%Y-%m-%d'),
            'subject': task.subject
        }
        for task in matching_tasks
    ]
    return JsonResponse(tasks_data, safe=False)



def main(request):
    return render(request, "index.html")

def vtask(request):
    t = taskshow.objects.all()
    return render(request, "vtask.html", {'t': t})



def taskviewer(request):
    if request.method == "POST":
        name = request.POST.get('task_name')
        description = request.POST.get('description')
        deadline=request.POST.get('deadline')
        subject=request.POST.get('subject')

        t = taskshow.objects.create(name=name, description=description,deadline=deadline,subject=subject)
        return redirect('vtask.html')
    return render(request, "task.html")
def home(request):
    return render(request, "dashboard.html")
def login(request):
    return render(request, "login.html")

def register(request):
    return  render(request,"register.html")



def sdetails(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        sign1 = registerdetails.objects.create(name=name, email=email, password=password)

    return render(request,"login.html")

def calendar(request):
    return render(request,"calendar.html")


def aboutus(request):
    return render(request, "aboutus.html")


def contactus(request):
    return render(request, "contactus.html")

def calendar_view(request):
    return render(request, "calendar.html")



