from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def home(request):
    context = {"is_logged_in": request.user.is_authenticated}
    return render(request, "home.html", context)


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        # Hardcoded credentials
        if username == "admin" and password == "admin":
            # Fake user login (for testing only)
            user, _ = User.objects.get_or_create(
                username="admin"
            )  # Create if doesn't exist
            auth_login(request, user)  # Log the user in
            return redirect("home")  # Redirect to home page

        return render(request, "login.html", {"error": "Invalid username or password"})

    return render(request, "login.html")


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists")
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.success(
                    request, "Account created successfully. Please log in."
                )
                return redirect("login")
        else:
            messages.error(request, "Passwords do not match")

    return render(request, "register.html")


def logout(request):
    auth_logout(request)
    return redirect("home")


# def register(request):
#     return render(request, "register.html")
