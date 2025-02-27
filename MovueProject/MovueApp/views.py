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
  
    movies=Movie.objects.get(movieid=id)
    print(movies)
    genre=movies.genre.all()
    review=ReviewRating.objects.filter(movieid=id).values()
    print(review)
    user=User.objects.get(id=1)
    if request.method=='POST':
    
        rating=request.POST['rating']
        review=request.POST['review']
        moviereview=ReviewRating(userid=user,movieid=movies,rating=rating,review=review)
        moviereview.save()
    
    context={"movies": movies,"movie_genres":  genre,"reviews": review }
       
    return render(request,'movie_list.html',context)

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

#fuction created for review

    
        




             
    
   
