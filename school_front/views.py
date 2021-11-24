from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"school_front/index.html")


def events(request):
    return render(request,"school_front/index.html")   

def contact(request):
    return render(request,"school_front/index.html")  

def training(request):
    return render(request,"school_front/index.html")     

def about(request):
    return render(request,"school_front/index.html")    