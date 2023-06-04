from django.db import models

from Home.models import Cloud_Site , DEPARTEMNTS 
from django.conf import settings


from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver


def Path_Users_Avatar_Profile(instance,filename):
    return "Cloud_Site/User_Profile/%s/user-img.jpeg"%(instance.user.id )





class User(AbstractUser):
    class Role(models.TextChoices):
        SuperVisor = "SUPERVISOR", "SuperVisor"
        SUPPORT = "SUPPORT", "Support"
        USERCLINET = "USERCLINET", "UserClint"

    base_role = Role.USERCLINET
    role = models.CharField(max_length=50, choices=Role.choices , default=base_role)
    Hospital = models.ForeignKey( Cloud_Site, blank=True, null=True , on_delete=models.SET_NULL,)
    DEPARTEMNT = models.ForeignKey( DEPARTEMNTS, blank=True, null=True , on_delete=models.SET_NULL, related_name='user_departement')

class USERCLINETManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.USERCLINET)


class User_Clint(User):

    base_role = User.Role.USERCLINET

    Clint = USERCLINETManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for Uer"
    


class SupportManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.SUPPORT)


class Support(User):

    base_role = User.Role.SUPPORT

    Support = SupportManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for Support"


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE , related_name='profile')
    bio = models.CharField(max_length=50, blank=True)
    avatar = models.FileField(upload_to=Path_Users_Avatar_Profile)
    
    def __str__(self):
       fir = str(self.user)
       if not self.user.first_name   :
           return fir
       else :
        return '%s %s' % (self.user.first_name, self.user.last_name)
    
    
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)
	instance.profile.save()
