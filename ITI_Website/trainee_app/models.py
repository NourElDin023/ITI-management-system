from django.db import models

# Create your models here.
class Trainee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    level = models.CharField(max_length=100)
    join_date = models.DateField()