from django.urls import path
from trainee_app.views import *

urlpatterns = [
    path("", trainee, name="trainee"),
    path("insert/", TraineeInsertView.as_view(), name="insert_trainee"),
    path("update/<int:id>/", traineeUpdate, name="update_trainee"),
    path("delete/<int:id>/", traineeDelete, name="delete_trainee"),
]
