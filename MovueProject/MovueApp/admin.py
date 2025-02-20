from django.contrib import admin # type: ignore
from .models import Movie, Genre, MovieGenre, ReviewRating, Reaction
#from .models import Watchlist

# Register your models here.

admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(MovieGenre)
admin.site.register(ReviewRating)
admin.site.register(Reaction)
#admin.site.register(Watchlist)
