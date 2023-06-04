
from django.db import models

from users.models import *
from django.conf import settings
# Create your models here.
def Path_PDF_Book(instance,filename):

    return "PDF_Book/%s.pdf"%(instance.title )

from django.test import TestCase

# Create your tests here.

class PDF_Book(models.Model):
    title = models.CharField(max_length=200  )
    summary = models.CharField(max_length=1000)
    pdf_book = models.FileField(blank=True, null=True, upload_to=Path_PDF_Book)
    add_by = models.ForeignKey(User,related_name='books',on_delete=models.CASCADE)
    created_dt = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    


class video_learning(models.Model):
    video_title = models.CharField(max_length=200  )
    video_summary = models.CharField(max_length=1000)
    youtube_link = models.CharField(max_length=1000)
    video_link = models.URLField()
    add_by = models.ForeignKey(User,related_name='user_add_video',on_delete=models.CASCADE)
    add_datet = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.video_title