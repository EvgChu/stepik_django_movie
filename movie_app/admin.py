 
from django.contrib import admin, messages
from .models import Movie, Director, Actor


admin.site.register(Director)
admin.site.register(Actor)
class RatingFilter(admin.SimpleListFilter):
    title = "filter rating"
    parameter_name = 'myfilter'
    def lookups(self, request, model_admin):
        return [
            ('<40', 'Low'),
            ('40-80', 'Medium'),
            ('>=80', 'Hight'),
        ]
    def  queryset(self, request, queryset):
        if self.value()=='<40':
            return queryset.filter(rating__lt=40)
        if self.value()=='40-80':
            return queryset.filter(rating__gte=40,rating__lt=80)
        if self.value()=='<40':
            return queryset.filter(rating__gte=80)
        return queryset

@admin.register(Movie) # Can use decorator
class MovieAdmin(admin.ModelAdmin):
    #fields = []
    exclude = [ 'slug' ]
    readonly_fields = ['currency_budget']
    list_display = ['name', 'rating', 'director','currency_budget',"rating_name"]
    list_editable = ['rating', 'director','currency_budget' ] # don't use name 
    ordering = ['-rating'] # for sorting
    list_per_page = 30 # pagination
    actions = ['set_dollars']
    search_fields = ['name__startswith', 'rating'] # 
    list_filter = ['name', 'rating', 'year',RatingFilter]
    filter_horizontal = ["actor"]

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
# 