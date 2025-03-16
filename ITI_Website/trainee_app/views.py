from django.shortcuts import render, redirect
from trainee_app.models import Trainee


# Create your views here.
def trainee(request):
    trainees = Trainee.objects.all()
    return render(request, "trainee.html", {"trainees": trainees})


def traineeInsert(request):
    if request.method == "POST":
        if (
            request.POST["traineeName"] == ""
            or request.POST["traineeAge"] == ""
            or request.POST["traineeLevel"] == ""
            or request.POST["join_date"] == ""
        ):
            return render(
                request,
                "insert_trainee.html",
                {"error": "Please fill in all the fields"},
            )
        name = request.POST["traineeName"]
        age = request.POST["traineeAge"]
        level = request.POST["traineeLevel"]
        join_date = request.POST["join_date"]
        Trainee.objects.create(name=name, age=age, level=level, join_date=join_date)
        return redirect("trainee")
    return render(request, "insert_trainee.html")


def traineeUpdate(request, id):
    traineeDetails = Trainee.objects.get(id=id)
    if request.method == "POST":
        if (
            request.POST["traineeName"] == ""
            or request.POST["traineeAge"] == ""
            or request.POST["traineeLevel"] == ""
            or request.POST["join_date"] == ""
        ):
            context = {}
            context["error"] = "Please fill in all the fields"
            context["trainee"] = traineeDetails
            return render(
                request,
                "update_trainee.html",
                context,
            )
        name = request.POST["traineeName"]
        age = request.POST["traineeAge"]
        level = request.POST["traineeLevel"]
        join_date = request.POST["join_date"]
        Trainee.objects.filter(id=id).update(
            name=name, age=age, level=level, join_date=join_date
        )
        return redirect("trainee")
    return render(request, "update_trainee.html", {"trainee": traineeDetails})


def traineeDelete(request, id):
    Trainee.objects.filter(id=id).delete()
    return redirect("trainee")
