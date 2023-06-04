from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from .models import *
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserDetailChangeForm
    template_name = "user/profile_edit.html"
