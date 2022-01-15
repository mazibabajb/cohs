from django.db import models




# Create your models here.
class Course(models.Model):
    course_category = (  
     ('cpd_training', 'cpd_training'),
     ('diploma', 'diploma'),
     ('short', 'short'),
     )
    category = models.CharField(
        choices=course_category,
        default='diploma',
        max_length=30)
    course_thumbnail = models.ImageField(upload_to='cars',default='default.png')    
    name = models.CharField(max_length=40)
    description = models.TextField(max_length=100)
    course_short_decsrpition = models.CharField(max_length=1000, blank=True)
    
    def __str__(self):
        return self.name


class Contact_us(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.IntegerField(default=0)
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.name


class Module(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    module_name = models.CharField(max_length=200)
    module_description = models.TextField(max_length=1000)

    def __str__(self):
        return self.module_name

class RegistrationForm(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    iD_Number = models.CharField(max_length=10)
    date_of_bith = models.DateField(auto_now=True)
    physical_address = models.CharField(max_length=300)
    postal_address = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.IntegerField(default=22)
    nk_first_name = models.CharField(max_length=100)
    nk_last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name


class Verication(models.Model):
    certificate_number = models.CharField(max_length=20)
    student_name = models.CharField(max_length=100)
    course_name = models.CharField(max_length=20)

    def __str__(self):
        return self.student_name





