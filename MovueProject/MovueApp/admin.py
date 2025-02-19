from django.contrib import admin # type: ignore
from .models import TableMovie,TableGenre,MovieGenre,Review,Reaction,Watchtable

# Register your models here.

admin.site.register(TableMovie)
admin.site.register(TableGenre)
admin.site.register(MovieGenre)
admin.site.register(Review)
admin.site.register(Reaction)
admin.site.register(Watchtable)
