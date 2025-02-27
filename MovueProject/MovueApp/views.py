from django.shortcuts import render,redirect
from .models import Movie,ReviewRating
from django.http import HttpResponse
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.
#function created for movie list

def movie_list(request):
    move=Movie.objects.all()
    
   
    context={"list":move}
    return render(request,"index.html",context)
 
#function for getting information about specific movie
@login_required(login_url="userlogin")
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





#fuction created for user authentication

def userlogin(request):
    err=None
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('movie_list')
        else:
            err="invalid credentials"
            print(err)
    return render(request,"login.html")  

def userlogout(request):
    logout(request)
    return redirect('userlogin')

def register(request):
    return redirect('register.html')      



    
        




             
    
   
