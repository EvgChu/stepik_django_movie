from locale import currency
import django
from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import slugify
# Create your models here.

class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    director_email = models.EmailField()

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

    def get_url(self):
        return  reverse('director-detail', args=[self.id])

class Actor(models.Model):
    MALE = "M"
    FEMALE = "F" 
    GENDERS = [
        (MALE, 'Man'),
        (FEMALE, 'Woman'), 
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDERS, default=MALE)

    def __str__(self) -> str:
        if self.gender == self.MALE:
            return f'Mr {self.first_name} {self.last_name}'
        else:
            return f'Mrs {self.first_name} {self.last_name}'

    def get_url(self):
        return  reverse('actor-detail', args=[self.id])
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

    director = models.ForeignKey(Director, on_delete=models.PROTECT, null=True)
    actor = models.ManyToManyField(Actor)
    # def save(self, *args, **kwargs) -> None:
    #     self.slug = slugify(self.name)
    #     return super(Movie, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.name} {self.rating}"

    def get_url(self):
        return  reverse('movie-detail', args=[self.slug])