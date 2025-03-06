from django.shortcuts import get_object_or_404, render,redirect
from .models import Movie,ReviewRating,Watchlist
from django.http import JsonResponse,HttpResponse
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Avg
from django.core.paginator import Paginator


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
    pages=Paginator(move, 5)
    pageno=request.GET.get('page')
    page_obj=pages.get_page(pageno)
    context={"list":page_obj}
    return render(request,"index.html",context)
   
    
 
#function for getting information about specific movie
@login_required(login_url="userlogin")
def information(request, id):
    use = request.user  # Get the currently logged-in user
    #print(use)

    # Get the movie or return a 404 if not found
    movies = get_object_or_404(Movie, movieid=id)
    #print(movies)

    # Get all genres associated with the movie
    genre = movies.genre.all()

    # Get all reviews for the movie
    
    review = ReviewRating.objects.exclude(userid_id=use).filter(movieid_id=id).values()
    if use:
        try:
            onereview=ReviewRating.objects.get(userid_id=use,movieid_id=id)
        except ReviewRating.DoesNotExist:
            review=ReviewRating.objects.filter(movieid_id=id).values() 
            onereview=None           

    if request.method == 'POST':
        rating = request.POST.get('rating')  # Use .get() to prevent KeyError
        review_text = request.POST.get('review')

        if rating and review_text:  # Ensure both rating and review are provided
            moviereview = ReviewRating(userid=use, movieid=movies, rating=rating, review=review_text)
            moviereview.save()

    # Get user's review for the movie
    userid = ReviewRating.objects.filter(userid=use, movieid=id).values()
    #print(userid)

    # Calculate the average rating
    avg = ReviewRating.objects.filter(movieid=id).aggregate(Avg("rating"))['rating__avg']

    # Handle the case where no ratings exist
    avgr = round(avg, 1) if avg is not None else 0

    context = {
        "movies": movies,
        "movie_genres": genre,
        "reviews": review,
        "use": userid,
        "average": avgr,
        "userev":onereview
    }

    return render(request, 'movie_list.html', context)



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
                
                
#function created for adding movie into wishlist

def watchlist(request):
    user=request.user
    useid=User.objects.get(username=user)
    print(useid)
   
    if request.method=='POST':
        movid=request.POST['movieid']
        mov=Movie.objects.get(movieid=movid)
        watch=Watchlist(userid=useid,movieid=mov)
        watch.save()
        return redirect('profile')
    
         
    return render(request,'profile.html')     

#function for search

def search(request):
    if request.method=='POST':
        search=request.POST.get('search')
        result=Movie.objects.filter(title__istartswith=search).values()
        print(result)
        if result:
            
            return render(request,'search_results.html',{'results':result})


        else:
            return redirect('movie_list')
    if not result:
        error="please enter a valid name"
        return redirect('movie_list',error)      

          
#function for user profile

def profile(request):
    usr=request.user
    prof=User.objects.filter(username=usr).values()
    
    context={'usrpro':prof}
    return render(request,'profile.html',context)


#function for  viewing watchlist

def vwatchlist(request):
    usr=request.user
    usid=User.objects.get(username=usr)
    uid=usid.id
    watch=Watchlist.objects.filter(userid_id=uid).values()
    movie_ids = []
    for w in watch:
        movie_ids.append(w['movieid_id']) 
    lis=Movie.objects.filter(movieid__in=movie_ids).values()
    print(lis)
    context={'movie':lis}
    return render(request,'profile.html',context)

#function for editing the review

def edit(request,id):
    newrev=ReviewRating.objects.get(reviewid=id)
    mid=newrev.movieid_id
    if request.method=='POST':
            nrev=request.POST.get('nrev')
            nrate=request.POST.get('nrate')
            newrev.rating=nrate
            newrev.review=nrev
            newrev.save()
    return redirect('information',id=mid)
    

#function for editing the review


 
    
        




             
    
   
