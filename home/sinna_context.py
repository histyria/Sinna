from quiz.models import *

from .models import *




def category_list (request):

    category_list = category.objects.all()
  
    context =  {

        'cat':category_list , 
       
        
        }
    return context
   