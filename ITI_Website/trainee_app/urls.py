from django.urls import path
from trainee_app.views import *

urlpatterns = [
    path("", trainee, name="trainee"),
    path("insert/", traineeInsert, name="insert_trainee"),
    path("update/", traineeUpdate, name="update_trainee"),
]
