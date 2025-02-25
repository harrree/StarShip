from django.shortcuts import render,redirect
from .models import Movie,ReviewRating,User
from django.http import HttpResponse


# Create your views here.
#function created for movie list
def movie_list(request):
    move=Movie.objects.all()
    
   
    context={"list":move}
    return render(request,"index.html",context)
 
#function for getting information about specific movie
def information(request,id):
    user=User.objects.get(id=id)
    movies=Movie.objects.get(movieid=id)
    genre=movies. genre.all()
    review=ReviewRating.objects.filter(movieid=id).values()
    print(user)
    context={"movies": movies,"movie_genres":  genre,"reviews": review,"user": user }
       
    return render(request,'movie_list.html',context)

    

#fuction created for review


