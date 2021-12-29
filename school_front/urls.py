from django.urls import path
from.import views

urlpatterns = [
    path('', views.home,name='home'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('events', views.events,name='events'),
    path('services', views.services,name='services'),
    path('cpd', views.cpd,name='cpd'),
    path('diploma_courses', views.diploma_courses,name='diploma_courses'),
    path('membership', views.membership,name='membership'),
    path('centres', views.centres,name='centres'),
    path('verify', views.verify,name='verify'),
    path('short_courses', views.short_courses,name='short_courses'),
    path('registation', views.registration,name='registraton'),
    path('course_detail/<int:id>/',views.course_detail, name="course_detail"),

    

]

