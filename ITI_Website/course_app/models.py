from django.db import models

# Create your models here.
class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()