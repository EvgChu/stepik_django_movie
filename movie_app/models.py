from locale import currency
import django
from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import slugify
# Create your models here.


class Movie(models.Model):
    USD = "USD"
    EUR = "EUR"
    RUB = "RUB"
    CURRENCY_CHOICES = [
        (EUR, 'Euro'),
        (USD, 'Dollars'),
        (RUB, 'Rubles'),
    ]

    name = models.CharField(max_length=40)
    rating = models.IntegerField(validators=[
                                            MinValueValidator(1),
                                            MaxValueValidator(100)
                                        ])
    year = models.IntegerField(null=True)
    budget = models.IntegerField(default=100000,validators=[
                                            MinValueValidator(1)
                                        ])
    currency_budget = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=RUB)
    slug = models.SlugField(default="", null=False)


    # def save(self, *args, **kwargs) -> None:
    #     self.slug = slugify(self.name)
    #     return super(Movie, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.name} {self.rating}"

    def get_url(self):
        return  reverse('movie-detail', args=[self.slug])