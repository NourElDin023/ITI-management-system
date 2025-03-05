from django.shortcuts import render


# Create your views here.
def course(request):
    courses = [
        {
            "id": 0,
            "name": "HTML",
            "level": "beginner",
            "start_date": "2023-01-01",
            "end_date": "2023-01-15",
        },
        {
            "id": 1,
            "name": "CSS",
            "level": "beginner",
            "start_date": "2023-01-16",
            "end_date": "2023-01-31",
        },
        {
            "id": 2,
            "name": "JavaScript",
            "level": "beginner",
            "start_date": "2023-02-01",
            "end_date": "2023-02-15",
        },
    ]

    return render(request, "course.html", {"courses": courses})
