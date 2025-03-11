from django.shortcuts import render, redirect
from course_app.models import Course

# Create your views here.
def course(request):
    courses = Course.objects.all()
    return render(request, "course.html", {"courses": courses})

def courseInsert(request):
    if request.method == "POST":
        name = request.POST["courseName"]
        level = request.POST["courseLevel"]
        start = request.POST["courseStart"]
        end = request.POST["courseEnd"]
        Course.objects.create(name=name, level=level, start_date=start, end_date=end)
        return redirect("course")
    return render(request, "insert_course.html")

def courseUpdate(request, id):
    courseDetails = Course.objects.get(id=id)
    if request.method == "POST":
        name = request.POST["courseName"]
        level = request.POST["courseLevel"]
        start = request.POST["courseStart"]
        end = request.POST["courseEnd"]
        Course.objects.filter(id=id).update(name=name, level=level, start_date=start, end_date=end)
        return redirect("course")
    return render(request, "update_course.html", {"course": courseDetails})

def courseDelete(request, id):
    Course.objects.filter(id=id).delete()
    return redirect("course")