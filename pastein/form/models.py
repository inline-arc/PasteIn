from configparser import MAX_INTERPOLATION_DEPTH
from pyexpat import model
from turtle import title
from django.db import models

# Create your models here.

class form(models.Model):
    title = models.CharField('title',max_length=100)
    link = models.URLField('links')
    textarea = models.TextField(blank=False)

    def __str__(self):
        return self.title #set model name 