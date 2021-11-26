from django.shortcuts import render
from.models import Courses

# Create your views here.
def home(request):
    return render(request,"school_front/index.html")

def events(request):
    return render(request,"school_front/events.html")   

def contact(request):
    return render(request,"school_front/Contact.html")  

def training(request):
    course = Courses.objects.all()
    context = {
        'courses' : course,
    }
    return render(request,"school_front/courses.html",context)     

def about(request):
    return render(request,"school_front/About.html")    

def services(request):
    return render(request,"school_front/service.html")    

def courses(request):
    return render(request,"school_front/course.html")          