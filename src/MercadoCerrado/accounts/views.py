from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from .forms import CreateUserForm

def register_view(request):
    form = CreateUserForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save()
        return redirect('/')
    context = {"form": form}
    return render(request, "accounts/singup.html", context)

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm(request)
    context = {
        "form": form
    }
    return render(request, "accounts/login.html", context)


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/")
    return render(request, "accounts/logout.html", {})