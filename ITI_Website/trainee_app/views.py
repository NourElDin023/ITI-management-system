from django.shortcuts import render


# Create your views here.
def trainee(request):
    trainees = [
        {
            "id": 0,
            "name": "Ahmed Hassan",
            "age": 23,
            "level": "beginner",
            "join_date": "2023-01-04",
        },
        {
            "id": 1,
            "name": "Ahmed Ali",
            "age": 20,
            "level": "beginner",
            "join_date": "2023-03-06",
        },
        {
            "id": 2,
            "name": "Mohamed Gamal",
            "age": 25,
            "level": "beginner",
            "join_date": "2023-02-02",
        },
    ]

    return render(request, "trainee.html", {"trainees": trainees})
