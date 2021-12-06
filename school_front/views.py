from django.shortcuts import render
from django.contrib import messages
from.models import Courses,Contact_us

# Create your views here.
def home(request):
    return render(request,"school_front/index.html")

def events(request):
    return render(request,"school_front/events.html")   

def contact(request):
    if request.method == 'POST':
        contact = Contact_us()
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        subject = request.POST.get('subject')
        contact.name = name
        contact.email = email
        contact.phone = phone
        contact.message = message
        contact.subject= subject
        contact.save()
        messages.success(request, 'your review has been sent thank you for your intrest')
    return render(request,"school_front/Contact.html")  

def training(request):
    courses = Courses.objects.all()
    context = {
        'courses' : courses,
    }
    return render(request,"school_front/courses.html",context)     

def about(request):
    return render(request,"school_front/About.html")    

def services(request):
    return render(request,"school_front/service.html")    

def courses(request):
    courses = Courses.objects.all()
    context = {
        'courses' : courses,
    }
    return render(request,"school_front/course.html",context)            