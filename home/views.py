from django.shortcuts import render
from .models import *
# Create your views here.

from users.models import User


def index(request):   
    usr = User.objects.all()
    gend = Profile.objects.all().values('gender')
    print(gend)
    return render(request, 'home/dashboard.html' ,{'usr':usr} )



def videos_list(request):   
    vid_list = video_learning.objects.all()
    return render(request, 'home/videos_list.html' ,{'vid_list':vid_list} )




def PDF_Book_list(request):   
    books_list = PDF_Book.objects.all()
    return render(request, 'home/PDF_Book.html' ,{'books_list':books_list} )



