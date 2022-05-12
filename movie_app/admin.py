from django.contrib import admin
from .models import Movie


@admin.register(Movie) # Can use decorator
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'year', "rating_name"]
    list_editable = ['rating', 'year' ] # don't use name 
    ordering = ['-rating'] # for sorting
    list_per_page = 30 # pagination

    @admin.display(ordering='rating', description="Status")
    def rating_name(self, movie:Movie):
        if movie.rating > 90:
            return "Great"
        elif movie.rating > 80:
            return "Nice"
        elif movie.rating > 60:
            return "Good"
        else:
            return "Bad"


# Register your models here.
# admin.site.register(Movie,MovieAdmin )