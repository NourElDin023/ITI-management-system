from django.urls import path
from course_app.views import *

urlpatterns = [
    path("", course, name="course"),
    path("insert/", courseInsert, name="insert_course"),
    path("update/<int:id>/", courseUpdate, name="update_course"),
    path("delete/<int:id>/", courseDelete, name="delete_course"),
]
