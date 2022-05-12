from django.shortcuts import render, get_object_or_404
from .models import Movie
# Create your views here.


def show_all_movie(request):
    movies = Movie.objects.all()
    return render(request,"all_movies.html",context={"movies":movies})


def show_one_movie(request, id_movie):
    movie = get_object_or_404(Movie,id=id_movie)
    context = {
        "movie": movie
        }
    return render(request,"one_movie.html",context=context)