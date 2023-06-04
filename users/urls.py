from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'users'
urlpatterns = [
    path('', views.index, name='index'),

    path('profile/', views.profile, name='profile'),

    # Authentication
    path('users/login/', views.UserLoginView.as_view(), name='login'),
    path('users/logout/', views.logout_view, name='logout'),
    path('users/register/', views.register, name='register'),
    path('users/password-change/', views.UserPasswordChangeView.as_view(), name='password_change'),
    path('users/password-change-done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='users/password_change_done.html'
    ), name="password_change_done"),
    path('users/password-reset/', views.UserPasswordResetView.as_view(), name='password_reset'),
    path('users/password-reset-confirm/<uidb64>/<token>/', 
        views.UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('users/password-reset-done/', auth_views.PasswordResetDoneView.as_view(
        template_name='users/password_reset_done.html'
    ), name='password_reset_done'),
    path('users/password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='users/password_reset_complete.html'
    ), name='password_reset_complete'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)