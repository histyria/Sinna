from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(User)
admin.site.register(User_STUDENT)
admin.site.register(User_TEACHER)
admin.site.register(Profile)