from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import login , authenticate, logout
from django.contrib import messages
from django.contrib.auth.views import LogoutView

# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("task_traker:task_list")
    else:
        form = UserCreationForm()
    return render(
        request, 
        template_name="auth_system/register.html",
        context= {"form": form}
    )

def log_in(request):
    if request.method == "POST":
        form  = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username , password=password)
            if user is not None:
                login(request,user)
                return redirect("task_traker:task_list")
            else:
                messages.error(request, "Wrong login or password.")
    else:
        form = AuthenticationForm()
    return render(
        request, 
        template_name="auth_system/log_in.html",
        context= {"form": form}
    )

def base(request):
    context = {

    }
    return render(
        request,
        "auth_system/register_login.html",
        context=context
    )

class CustomLogoutView(LogoutView):
    next_page = 'base'
    