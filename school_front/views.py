from django.shortcuts import render,redirect
from django.contrib import messages
from.models import *
from.models import RegistrationForm

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
        contact.name = name
        contact.email = email
        contact.phone = phone
        contact.message= message
        contact.save()
        messages.success(request, 'Thank you for contacting us your message has been received')
    return render(request,"school_front/contact.html")      

 

def about(request):
    return render(request,"school_front/About.html")    

def services(request):
    return render(request,"school_front/service.html")    

def cpd(request):
    courses = Course.objects.filter(category='cpd_training')
    context = {
        'courses' : courses,
    }
    return render(request,"school_front/cpd.html",context)     


def diploma_courses(request):
    courses = Course.objects.filter(category='diploma')
    context = {
        'courses' : courses,
    }
    return render(request,"school_front/diploma_course.html",context)    


def short_courses(request):
    courses = Course.objects.filter(category='short')
    context = {
        'courses' : courses,
    }
    return render(request,"school_front/short_course.html",context)    

def course_detail(request, id):
    modules = Module.objects.all()
    course = Course.objects.get(id=id)
    context = {
		'course': course,
        'modules': modules
	}
    return render(request,"school_front/course_detail.html",context)    

def membership(request):
    return render(request,"school_front/membership.html")

def centres(request):
    return render(request,"school_front/centres.html")


def verify(request):
    
    certificate_number = request.POST.get("certificate_number")

    certificate = Verication.objects.filter(certificate_number=certificate_number) 
    if certificate  != certificate_number:
        messages.error(request,"The certtficate could not be found")
    else:
        messages.success(request,"This is an authentic cohs certificate")
        
    return render(request,"school_front/verify.html")


    


def registration(request):
    if request.method == 'POST':
        register = RegistrationForm()
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        iD_Number = request.POST.get('iD_Number')
        date_of_bith = request.POST.get('date_of_bith')
        physical_address = request.POST.get('physical_address')
        postal_address = request.POST.get('postal_address')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        nk_first_name = request.POST.get('nk_first_name')
        nk_last_name = request.POST.get('nk_last_name')
        register.first_name = first_name
        register.last_name = last_name
        register.iD_Number  = iD_Number 
        register.date_of_bith = date_of_bith
        register.physical_address = physical_address
        register.postal_address = postal_address
        register.email = email
        register.phone_number = phone_number
        register.nk_first_name = nk_first_name
        register.nk_last_name = nk_last_name
        register.save()
        messages.success(request, "You have been successfuly registered")
    return render(request,"school_front/register.html")    