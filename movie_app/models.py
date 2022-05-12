import django
from django.db import models
from django.urls import reverse

from django.utils.text import slugify
# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=40)
    rating = models.IntegerField()
    year = models.IntegerField(null=True)
    budget = models.IntegerField(default=100000)
    slug = models.SlugField(default="", null=False)


    def save(self, *args, **kwargs) -> None:
        self.slug = slugify(self.name)
        return super(Movie, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.name} {self.rating}"

    def get_url(self):
        return  reverse('movie-detail', args=[self.slug])