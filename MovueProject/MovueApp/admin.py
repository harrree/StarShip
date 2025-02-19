from django.contrib import admin
from .models import User,TableMovie,TableGenre,MovieGenre,Review,Reaction,Watchtable

# Register your models here.
admin.site.register(User)
admin.site.register(TableMovie)
admin.site.register(TableGenre)
admin.site.register(MovieGenre)
admin.site.register(Review)
admin.site.register(Reaction)
admin.site.register(Watchtable)
