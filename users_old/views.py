from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from .models import *
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.template.loader import render_to_string
from django.http import JsonResponse , HttpResponse

from django.contrib.auth import authenticate, login, logout

# Create your views here.
def login_view(request):
    # future -> ?next=/articles/create/
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            
    else:
        form = AuthenticationForm(request)
    context = {
        "form": form
    }
    return render(request, "registration/login.html", context)


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/login/")
    return render(request, "accounts/logout.html", {})

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserDetailChangeForm
    template_name = "users/profile.html"


def register(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        DEPARTEMNT = request.POST.get('DEPARTEMNT')
        print(DEPARTEMNT)
        if form.is_valid():
            user = form.save()
        
            user.save()
            auth_login(request,user)
            return redirect('Home:index')

        else:
            for error in list(form.errors.values()):
                print(request, error)

    else:
        form = UserRegistrationForm()

    return render(request=request, template_name = "registration/sign_up.html", context={"form": form} )


def Get_Departement(request):
    id_Hospital = request.GET.get('id_Hospital')
    get_dep = DEPARTEMNTS.objects.filter(Dep_Site__id = id_Hospital )
    data = render_to_string('accounts/dep.html',{'data': get_dep},request=request)
    return JsonResponse(data , safe=False)