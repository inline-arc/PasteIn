

from django.urls import path, include
from . import views 

urlpatterns = [
        path('',views.form,name="form"),
        path('shit',views.listshit,name="lshit"),
]
