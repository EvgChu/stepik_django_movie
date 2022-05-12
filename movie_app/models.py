from django.db import models

# Create your models here.


class Movie(models.Movie):
    name = models.CharField(max_length=40)
    rating = models.IntegerField()