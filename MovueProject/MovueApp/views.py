from django.shortcuts import get_object_or_404, render,redirect
from .models import Movie,ReviewRating,Watchlist,Genre
from django.http import JsonResponse,HttpResponse
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,AnonymousUser
from django.db.models import Avg,Count
from django.core.paginator import Paginator
from django.contrib import messages
from .utils import youtubetrailer


# Create your views here.

#fuction created for user authentication

def userlogin(request):
   
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
           messages.error(request,"invalid credentials")
    else:
        user=None       
            
    return render(request,"login.html") 
#function created for movie list

def movie_list(request):
    move=Movie.objects.all()
    most=ReviewRating.objects.annotate(avgrate=Avg('rating')).filter(avgrate__gt = 3.5).distinct().values('movieid')
    popuplar=[]
    for mov in most:
        popuplar.append(mov['movieid'])
   
    popularmovies=Movie.objects.filter(movieid__in=popuplar)
    genre=Genre.objects.all()

    context={"list":move,"popularmove":popularmovies,"genres": genre}
    return render(request,"index.html",context)
   
    
 
#function for getting information about specific movie

def information(request, id):
    use = request.user if not isinstance(request.user, AnonymousUser) else None  # Get the currently logged-in user
    #print(use)

    # Get the movie or return a 404 if not found
    movies = get_object_or_404(Movie, movieid=id)
    #print(movies.title)
    trailer=youtubetrailer(movies.title)

    # Get all genres associated with the movie
    genre = movies.genre.all()

    # Get all reviews for the movie
   
    review = ReviewRating.objects.exclude(userid_id=use).filter(movieid_id=id).select_related('userid')
    for reviews in review:
        reviews.range = range(1, 6)
    onereview=None
    if use:
        try:
           onereview=ReviewRating.objects.get(userid_id=use,movieid_id=id)
        except ReviewRating.DoesNotExist:
             onereview=None
             
    else:
        messages.info(request,"you can only write review after login.")         
                      
# Get user's review for the movie
    userid = ReviewRating.objects.filter(userid=use, movieid=id).values()
    #print(userid)

    # Calculate the average rating
    avg = ReviewRating.objects.filter(movieid=id).aggregate(Avg("rating"))['rating__avg']

    # Handle the case where no ratings exist
    avgr = round(avg, 1) if avg is not None else 0
    try:
        already_in_watch=Watchlist.objects.get(userid_id=use,movieid_id=id)
        dont_add=True
    except Exception:
        dont_add=False

    if dont_add is True:
        cannot=dont_add 
    else:
        cannot=False       

    context = {
        "movies": movies,
        "movie_genres": genre,
        "reviews": review,
        "use": userid,
        "average": avgr,
        "userev":onereview,
        "cannot_add":cannot,
        "movie_trailer":trailer
       
    }

    return render(request, 'movie_list.html', context)

#fuction created for user review
@login_required(login_url="userlogin")
def review(request,id):
    
    use=request.user
    movies = get_object_or_404(Movie, movieid=id)

    if request.method == 'POST':
        rating = request.POST.get('rating')  # Use .get() to prevent KeyError
        review_text = request.POST.get('review')

        if rating and review_text:  # Ensure both rating and review are provided
            moviereview = ReviewRating(userid=use, movieid=movies, rating=rating, review=review_text)
            moviereview.save()

            #response={'review':review_text,'rating':rating}
    return redirect('information',id)
     




#fuction created for user logout

def userlogout(request):
    logout(request)
    return redirect('movie_list')

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
    results=Movie.objects.all()
    if request.method=='POST':
        search=request.POST.get('search')
        genr=request.POST.get('genre')
        print(search)
        
        if search:
            results=results.filter(title__istartswith=search)
        if genr:
            results=results.filter(genre=genr)    
        if results:
            paginator=Paginator(results,2)
            page_number=request.GET.get('page',1)
            print(f"Page number: {page_number}")
            page_obj=paginator.get_page(page_number)
            genre=Genre.objects.all()
    
            print(f"Page object: {page_obj}")
            context={"page_obj":page_obj, "genres": genre }
            return render(request,'search_results.html',context)
        else:
            return redirect('movie_list')
    if not results:
        results=None
        messages.error(request,"please enter a valid name")
        return redirect('movie_list')      
    return redirect('movie_list')
#function for user profile

def profile(request):
    usr=request.user
    prof=User.objects.filter(username=usr).values()
    cont=Watchlist.objects.filter(userid=usr).values('movieid').distinct().count()
    watchlistcont=cont if cont else 0
    count=ReviewRating.objects.filter(userid=usr).values('movieid').distinct().count()
    moviecount=count if count else 0
    usid=User.objects.get(username=usr)
    uid=usid.id

#getting the user watchlist

    watch=Watchlist.objects.filter(userid_id=uid).values()
    if watch:
        movie_ids = []
        for w in watch:
          movie_ids.append(w['movieid_id'])
          
        lis=Movie.objects.filter(movieid__in=movie_ids)
        print(lis)
    else:
        lis=None    

#getting the user reviewed movie

    rev=ReviewRating.objects.filter(userid=uid).values('movieid')
    if rev:
      movie=[]
      for movielist in rev:
          movie.append(movielist['movieid'])
      list=Movie.objects.filter(movieid__in=movie)
        
      print("movie")
      print(list)
    else:
        list=None  
    
    context={'usrpro':prof,'count':moviecount,'watchlistcount':watchlistcont,'movie':lis,'reviews':list}
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
            response={'review':nrev,'rating':nrate}
    return JsonResponse(response)
    

#function for deleting  the review

def dele(request,id):
    
    movid=ReviewRating.objects.get(reviewid=id)
    ids= movid.movieid_id
    review=ReviewRating.objects.get(reviewid=id)
    review.delete()
    return redirect('information',id=ids)


 #function created for edit profile 

def editprofile(request):
    if request.method=='POST':
        useid=request.POST.get('userid')
        username=request.POST.get('username')
        firstname=request.POST.get('first_name')
        lastname=request.POST.get('last_name')
        email=request.POST.get('email')
        user=User.objects.get(id=useid)
        if user:
            try:
                user.username=username
                user.first_name=firstname
                user.last_name=lastname
                user.email=email
                user.save()
                return redirect('userlogin')
            except Exception as e:
                 messages.error(request,"already exist")

        else:
            messages.error(request,"not updated")
            return redirect('profile')

    return redirect('profile')    
       



    
        




             
    
   
