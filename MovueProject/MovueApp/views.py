from django.shortcuts import render,redirect
from .models import Movie,ReviewRating
from django.http import JsonResponse
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.

#fuction created for user authentication

def userlogin(request):
    err=None
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        #id= User.objects.filter(username=username).values_list('id')
        #request.session['userid']=id       
        if user:
            login(request,user)
            return redirect('movie_list')
        else:
            err="invalid credentials"
            print(err)
    return render(request,"login.html") 
#function created for movie list

def movie_list(request):
    move=Movie.objects.all()
    context={"list":move}
    return render(request,"index.html",context)
   
    
 
#function for getting information about specific movie
@login_required(login_url="userlogin")
def information(request,id):
    #uid= request.session.get('userid')
    use=request.user
    print(use)
  
    movies=Movie.objects.get(movieid=id)
    print(movies)
    genre=movies.genre.all()
    review=ReviewRating.objects.filter(movieid=id).values()
    #print(review)
    #user=User.objects.get(id=2)
    #print(user)
    if request.method=='POST':
    
         rating=request.POST['rating']
         review=request.POST['review']
         moviereview=ReviewRating(userid=use,movieid=movies,rating=rating,review=review)
         moviereview.save()
    userid=ReviewRating.objects.filter(userid=use,movieid=id).values()
    print(userid)     
    
    context={"movies": movies,"movie_genres":  genre,"reviews": review,"use":userid }
       
    return render(request,'movie_list.html',context)


#fuction created for user logout

def userlogout(request):
    logout(request)
    return redirect('userlogin')

#fuction created for user registeration

def register(request):
    if request.method=='POST':
        firstname=request.POST.get('first_name')
        lastname=request.POST.get('last_name')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')

        if password==cpassword:
            if User.objects.filter(username=username).exists():
                print("username exist")
            else: 
                user=User.objects.create_user(username=username,email=email,password=password,first_name=firstname,last_name=lastname)
                user.save()
                return redirect('userlogin')
            
    return render(request,'register.html')             
                
                

          



    
        




             
    
   
