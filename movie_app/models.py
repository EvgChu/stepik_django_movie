from django.db import models
from django.urls import reverse
# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=40)
    rating = models.IntegerField()
    year = models.IntegerField(null=True)
    budget = models.IntegerField(default=100000)


    def __str__(self) -> str:
        return f"{self.name} {self.rating}"

    def get_url(self):
        return  reverse('movie-detail', args=[self.id])