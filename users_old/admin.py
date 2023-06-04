from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(User_Clint)

admin.site.register(Support)
admin.site.register(Profile)
admin.site.register(User)