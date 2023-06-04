from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
app_name = 'users'
urlpatterns = [
    path('<int:pk>/edit/', ProfileUpdateView.as_view(), name='profile-edit'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('Profile_user/', ProfileUpdateView.as_view(),name='profile-edit'),
    path("register/", register, name="user_register"),
    path('loginss/',login_view,name='losgin'),
    path('login/',auth_views.LoginView.as_view(template_name='registration/login.html'),name='login'),
    path('settings/change_password/',auth_views.PasswordChangeView.as_view(template_name='registration/password_reset.html'),name='password_change'),
    path('settings/change_password/done/',auth_views.PasswordChangeDoneView.as_view(template_name='registration/change_password_done.html'),name='password_change_done'),
]