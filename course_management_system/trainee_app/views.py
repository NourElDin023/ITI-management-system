from django.shortcuts import render, redirect
from trainee_app.models import Trainee
from course_app.models import Course
from django.shortcuts import get_object_or_404
from django.views import View


# Create your views here.
def trainee(request):
    trainees = Trainee.objects.all()
    return render(request, "trainee.html", {"trainees": trainees})


class TraineeInsertView(View):
    def get(self, request):
        courses = Course.objects.all()
        return render(request, "insert_trainee.html", {"courses": courses})

    def post(self, request):
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
        selected_courses = request.POST.getlist("traineeCourses")
        trainee = Trainee.objects.create(
            name=name, age=age, level=level, join_date=join_date
        )
        print(selected_courses)

        if selected_courses:
            trainee.courses.set(Course.objects.filter(id__in=selected_courses))

        return redirect("trainee")


# def traineeInsert(request):
#     if request.method == "POST":
#         if (
#             request.POST["traineeName"] == ""
#             or request.POST["traineeAge"] == ""
#             or request.POST["traineeLevel"] == ""
#             or request.POST["join_date"] == ""
#         ):
#             return render(
#                 request,
#                 "insert_trainee.html",
#                 {"error": "Please fill in all the fields"},
#             )
#         name = request.POST["traineeName"]
#         age = request.POST["traineeAge"]
#         level = request.POST["traineeLevel"]
#         join_date = request.POST["join_date"]
#         selected_courses = request.POST.getlist("traineeCourses")
#         trainee = Trainee.objects.create(
#             name=name, age=age, level=level, join_date=join_date
#         )
#         print(selected_courses)

#         if selected_courses:
#             trainee.courses.set(Course.objects.filter(id__in=selected_courses))

#         return redirect("trainee")
#     courses = Course.objects.all()
#     return render(request, "insert_trainee.html", {"courses": courses})


def traineeUpdate(request, id):
    trainee = get_object_or_404(Trainee, id=id)
    courses = Course.objects.all()
    selected_courses = trainee.courses.values_list("id", flat=True)

    if request.method == "POST":
        if (
            request.POST["traineeName"] == ""
            or request.POST["traineeAge"] == ""
            or request.POST["traineeLevel"] == ""
            or request.POST["join_date"] == ""
        ):
            return render(
                request,
                "update_trainee.html",
                {
                    "trainee": trainee,
                    "courses": courses,
                    "selected_courses": selected_courses,
                    "error": "Please fill in all fields",
                },
            )

        # ✅ Update trainee info
        trainee.name = request.POST["traineeName"]
        trainee.age = request.POST["traineeAge"]
        trainee.level = request.POST["traineeLevel"]
        trainee.join_date = request.POST["join_date"]

        # ✅ Update courses
        selected_courses = request.POST.getlist("traineeCourses")
        trainee.courses.set(Course.objects.filter(id__in=selected_courses))

        trainee.save()

        return redirect("trainee")

    return render(
        request,
        "update_trainee.html",
        {
            "trainee": trainee,
            "courses": courses,
            "selected_courses": selected_courses,
        },
    )


def traineeDelete(request, id):
    Trainee.objects.filter(id=id).delete()
    return redirect("trainee")
