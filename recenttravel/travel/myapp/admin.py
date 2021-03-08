from django.contrib import admin
from myapp.models import *
# Register your models here.
mymodule = [Slider, Post, Contact]
admin.site.register(mymodule)
