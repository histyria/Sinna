from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Home.models import *

from .models import *


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import AuthenticationForm


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(help_text='A valid email address, please.', required=True)

    class Meta:
        model =  User
        fields = ['first_name', 'last_name', 'username' , 'Hospital' , 'DEPARTEMNT', 'email', 'password1', 'password2']
    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['DEPARTEMNT'].widget.attrs['DEPARTEMNT'] = "DEPARTEMNT-dev"
        # add a "form-control" class to each form input
        # for enabling bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })
        self.fields['DEPARTEMNT'].queryset = DEPARTEMNTS.objects.none()
        if 'DEPARTEMNT' in self.data:
            self.fields['DEPARTEMNT'].queryset = DEPARTEMNTS.objects.all()
        elif self.instance.pk:
            self.fields['DEPARTEMNT'].queryset = DEPARTEMNTS.objects.all().filter(pk=self.instance.DEPARTEMNT.pk)
    
    def clean_user_name(self):
        Username = self.cleaned_data['Username'].lower()
        r = User.objects.filter(Username=Username)
        if r.count():
            raise forms.ValidationError("Username already exists")
        return Username
    

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Please use another Email, that is already taken')
        return email

class LoginForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput())


    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({'class': 'form-control',})


    class Meta:
        model = User
        fields = ('username', 'password', 'remember_me')

class ProfileForm(forms.ModelForm):
   
    class Meta:
        model = Profile
        fields = ('__all__')

class UserDetailChangeForm(forms.ModelForm):
    

    class Meta:
        model = User
        fields = '__all__'