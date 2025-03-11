from django.shortcuts import render
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
    return render(request, "insert_course.html")

def courseUpdate(request):
    return render(request, "update_course.html")