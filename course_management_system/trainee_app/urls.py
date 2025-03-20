from django.urls import path
from trainee_app.views import *

urlpatterns = [
    path("", TraineeListView.as_view(), name="trainee"),
    path("insert/", TraineeInsertView.as_view(), name="insert_trainee"),
    path("update/<int:id>/", TraineeUpdateView.as_view(), name="update_trainee"),
    path("delete/<int:pk>/", TraineeDeleteView.as_view(), name="delete_trainee"),
]
