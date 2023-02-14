from django.contrib import admin
from .models import Category, Genre, Movie, MovieShots, Actors, RatingsStar, Rating, Reviews

admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(MovieShots)
admin.site.register(Actors)
admin.site.register(RatingsStar)
admin.site.register(Rating)
admin.site.register(Reviews)
# Register your models here.
