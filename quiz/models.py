from django.db import models
from users.models import User
class category(models.Model):
    category_name = models.CharField(max_length=200, verbose_name ="إسم القسم | Category Name" )
    summary = models.CharField(max_length=1000, verbose_name ="نبذه مختصره عن القسم | Description From Category ")
    def __str__(self):
        return self.category_name
    

class Content(models.Model):
    title = models.CharField(max_length=200 )
    category = models.ForeignKey(category, on_delete=models.CASCADE  , verbose_name ="إسم القسم | Category Name" )
    pic_book=models.ImageField(blank=True, null=True, upload_to='Content/Content_image')
    pdf_File = models.FileField(blank=True, null=True, upload_to='Content/Content_pdf')
    created_by = models.ForeignKey(User,related_name='teachers',on_delete=models.CASCADE)
    created_dt = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.title