from django.shortcuts import render

# Create your views here.
def trainee(request):
    return render(request,'trainee.html')