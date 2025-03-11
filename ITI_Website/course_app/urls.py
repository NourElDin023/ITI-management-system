from django.urls import path
from course_app.views import *

urlpatterns = [
    path("", course, name="course"),
    path("insert/", courseInsert, name="insert_course"),
    path("update/", courseUpdate, name="update_course"),
]
