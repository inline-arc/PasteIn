from django.shortcuts import render
from .models import form as list
# Create your views here.

def listshit(request):
    shitls = list.objects.all()
    return render(request, 'shit.html',{'shitls': shitls })

def form(request):
    return render(request, 'form.html', {})
