from django.db import models



# Create your models here.
class Courses(models.Model):
    Course_thumbnail = models.FileField(blank=True)
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=100)
    course_short_decsrpition = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.name


class Contact_us(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.IntegerField(default=0)
    subject = models.CharField(max_length=500)
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.name
    
