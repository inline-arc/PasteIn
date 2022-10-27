from django.contrib import admin
# Register your models here.
#import model first with name 
from .models import form


#register site
admin.site.register(form) #admin site 