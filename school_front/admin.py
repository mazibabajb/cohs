from django.contrib import admin
from.models import Course, Contact_us,Module,RegistrationForm,Verication

admin.site.site_header = 'COHS ADMIN DASHBOARD'
# Register your models here.
admin.site.register(Course)
admin.site.register(Contact_us)
admin.site.register(Module)
admin.site.register(RegistrationForm)
admin.site.register(Verication)