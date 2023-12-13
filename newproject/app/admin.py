from django.contrib import admin
from .models import *

# Register your models here.
class Studentregister(admin.ModelAdmin):
    list_display = ['id','name','email','roll_no','adress']

admin.site.register(Students,Studentregister)