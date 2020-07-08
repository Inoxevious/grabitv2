from django.contrib import admin

# Register your models here.
# *coding: utf-8*

from .models import *
admin.site.register(User)
admin.site.register(Package)