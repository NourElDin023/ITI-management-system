from django.shortcuts import render
from trainee_app.models import Trainee

# Create your views here.
def trainee(request):
    trainees = Trainee.objects.all()
    return render(request, "trainee.html", {"trainees": trainees})

def traineeInsert(request):
    if request.method == "POST":
        name = request.POST["traineeName"]
        age = request.POST["traineeAge"]
        level = request.POST["traineeLevel"]
        joinDate = request.POST["joinDate"]
        Trainee.objects.create(name=name, age=age, level=level, join_date=joinDate)
    return render(request, "insert_trainee.html")

def traineeUpdate(request):
    return render(request, "update_trainee.html")