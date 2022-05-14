from django.shortcuts import render, get_object_or_404
from .models import Actor, Movie, Director
from django.db.models import Value
# Create your views here.


def show_all_movie(request):
    movies = Movie.objects.annotate(new_field=Value(True))
    return render(request,"all_movies.html",context={"movies":movies})

def show_all_directors(request):
    directors = Director.objects.all()
    return render(request,"all_directors.html",context={"directors":directors})

def show_all_actors(request):
    actors = Actor.objects.all()
    return render(request,"all_actors.html",context={"actors":actors})

def show_one_movie(request, slug_movie:str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    context = {
        "movie": movie
        }
    return render(request,"one_movie.html",context=context)

def show_one_director(request, id_director:int):
    director = get_object_or_404(Director, id=id_director)
    context = {
        "director": director
        }
    return render(request,"one_director.html",context=context)

def show_one_actor(request, id_actor:int):
    actor = get_object_or_404(Actor, id=id_actor)
    context = {
        "actor": actor
        }
    return render(request,"one_actor.html",context=context)