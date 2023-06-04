from django.urls import path
from .views import *
app_name = 'home'
urlpatterns = [
    path('', index, name="index"),
    path('videos_list/', videos_list, name="videos_list"),
    path('PDF_Book_list/', PDF_Book_list, name="PDF_Book_list"),
   
]