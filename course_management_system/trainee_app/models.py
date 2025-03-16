from django.db import models
from course_app.models import Course


# Create your models here.
class Trainee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    level = models.CharField(max_length=100)
    join_date = models.DateField()
    courses = models.ManyToManyField(Course, blank=True)