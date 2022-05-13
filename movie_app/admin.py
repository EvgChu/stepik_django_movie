 
from django.contrib import admin, messages
from .models import Movie


@admin.register(Movie) # Can use decorator
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'year', 'currency_budget',"rating_name"]
    list_editable = ['rating', 'year','currency_budget' ] # don't use name 
    ordering = ['-rating'] # for sorting
    list_per_page = 30 # pagination
    actions = ['set_dollars']

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
            
    @admin.action(description="Set dollars")
    def set_dollars(self,request, qs):
        cnt_res = qs.update(currency_budget=Movie.USD)
        self.message_user(
            request,
            f" Update {cnt_res}",
            messages.ERROR
        )

# Register your models here.
# admin.site.register(Movie,MovieAdmin )