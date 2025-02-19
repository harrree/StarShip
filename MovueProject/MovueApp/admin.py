from django.contrib import admin # type: ignore
from .models import Movie,Genre,MovieGenre,Review,Reaction,Watchtable

# Register your models here.

admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(MovieGenre)
admin.site.register(Review)
admin.site.register(Reaction)
admin.site.register(Watchtable)
