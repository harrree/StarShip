from django.shortcuts import render,redirect
from .models import Movie


# Create your views here.
def movie_list(request):
    move=Movie.objects.all()
   
    context={"list":move}
    return render(request,"index.html",context)


def information(request,id):
    
    movies=Movie.objects.get(movieid=id)

    genre=movies. genre.all()
    print( movies. genre.all())
    
    context={"movies": movies,"movie_genres":  genre }
    return render(request,'movie_list.html',context)

 