from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views import View


# Create your views here.
def home(request):
    context = {"is_logged_in": request.user.is_authenticated}
    return render(request, "home.html", context)


class UserRegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, "register.html", {"form": form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after registration
            return redirect("trainee")  # Redirect to trainee list or dashboard
        return render(request, "register.html", {"form": form})

    # ✅ Login View


class UserLoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, "login.html", {"form": form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("trainee")  # Redirect to trainee list or dashboard
        return render(request, "login.html", {"form": form})


# ✅ Logout View
def user_logout(request):
    logout(request)
    return redirect("login")  # Redirect to login page after logout
