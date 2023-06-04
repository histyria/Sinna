from django.db import models

from django.conf import settings

from django.conf.urls.static import static

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver


def Path_Users_Avatar_Profile(instance,filename):
    return "User_Profile/%s/user-img.jpeg"%(instance.user.id )





class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        STUDENT = "STUDENT", "Student"
        TEACHER = "TEACHER", "Teacher"

    base_role = Role.STUDENT
    role = models.CharField(max_length=50, choices=Role.choices , default=base_role)
   

class USERSTUDENTTManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.STUDENT)


class User_STUDENT(User):

    base_role = User.Role.STUDENT

    STUDENT = USERSTUDENTTManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for Uer"
    


class TEACHERManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.TEACHER)


class User_TEACHER(User):

    base_role = User.Role.TEACHER

    TEACHER = TEACHERManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for TEACHER"






def Path_Profile_Avatar(instance,filename):
    

    return "media/%s/Users/avataer/%s/avatar.jpeg"%(instance.user.id ,instance.user.id)

   
class Profile(models.Model):
    class Gender_Role(models.TextChoices):
        MALE = "MALE", "Male"
        FEMALE = "FEMALE", "Female"

    
    user = models.OneToOneField(User, on_delete=models.CASCADE , related_name='profile')
    bio = models.CharField(max_length=50, blank=True)
    avatar = models.FileField(upload_to=Path_Profile_Avatar)
    birthday = models.DateField(null=True, blank=True)
    gender_role = Gender_Role.MALE
    gender = models.CharField(max_length=50, choices=Gender_Role.choices , default=gender_role)
    def __str__(self):
       fir = str(self.user)
       if not self.user.first_name   :
           return fir
       else :
        return '%s %s' % (self.user.first_name, self.user.last_name)
    @property
    def get_avatar(self):
        return self.avatar.url if self.avatar else static('img/team/default-profile-picture.png')
  

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)
	instance.profile.save()
