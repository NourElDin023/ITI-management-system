from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views import View
from django.contrib import messages


# Create your views here.
def home(request):
    context = {"is_logged_in": request.user.is_authenticated}
    return render(request, "home.html", context)


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful! You can now log in.")
            return redirect("login")
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        form = UserCreationForm()

    return render(request, "register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password. Please try again.")

    return render(request, "login.html")


def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("login")
