from django.contrib import admin
# Register your models here.

from .models import form


#register site
admin.site.register(form)