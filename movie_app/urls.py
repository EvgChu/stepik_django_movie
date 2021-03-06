"""movie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_all_movie, name='main'),
    path('movie/<str:slug_movie>', views.show_one_movie, name="movie-detail"),
    path('directors', views.show_all_directors, name='directors-main'),
    path('directors/<int:id_director>', views.show_one_director, name="director-detail"),
    path('actor', views.show_all_actors, name='actors-main'),
    path('actor/<int:id_actor>', views.show_one_actor, name="actor-detail"),
]
