from django.shortcuts import render


# Create your views here.
def home(request):
    context = {
        "is_logged_in": False
    }
    return render(request, "home.html", context)


def login(request):
    return render(request, "login.html")


def register(request):
    return render(request, "register.html")
