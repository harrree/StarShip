from django.shortcuts import get_object_or_404, render,redirect
from .models import Movie,ReviewRating,Watchlist,Genre,UserProfile,Reaction
from django.http import JsonResponse,HttpResponse
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,AnonymousUser
from django.db.models import Avg,Count
from django.core.paginator import Paginator
from django.contrib import messages
from .utils import youtubetrailer
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator

# Create your views here.

#fuction created for user authentication

def userlogin(request):
   
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        #id= User.objects.filter(username=username).values_list('id')
        #request.session['userid']=id 
        has_error=False
        if not username:
            messages.error(request,"Please enter username")
            has_error=True
        if not password:
            messages.error(request,"please enter valid password")
            has_error=True
        if has_error:
            return redirect('userlogin')      
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
        bio = request.POST.get('bio') 
        profile_picture = request.FILES.get('profile_picture')  
        has_error=False
        
        if not username:
            messages.error(request,"Enter valid username")
            has_error=True 
        if not firstname:
            messages.error(request,"Enter valid firstname")
            has_error=True   
        if not lastname:
            messages.error(request,"Enter valid lastname")
            has_error=True
        if not password:
            messages.error(request,"Enter valid password")
            has_error=True
        if not cpassword:
            messages.error(request,"please confirm password")
            has_error=True             
        if not email:
            messages.error(request,"Enter valid email")
            has_error=True  
        else:
            try:
                EmailValidator()(email) 
            except ValidationError:
                 messages.error(request, "Invalid email format.")
                 has_error=True                       
        
        if has_error:
            return redirect('register')
        

        if password==cpassword:
            if User.objects.filter(username=username).exists():
                print("username exist")
            else: 
                user=User.objects.create_user(username=username,email=email,password=password,first_name=firstname,last_name=lastname)
                user.save()

                profile=UserProfile.objects.create(user=user,bio=bio,profile_picture=profile_picture)
                return redirect('userlogin')
            
    return render(request,'register.html')             
                
                
#function created for adding movie into wishlist
@login_required(login_url="userlogin")
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
    genre=Genre.objects.all()
    if request.method=='GET':
        search_term=request.GET.get('search')
        selected_genres = request.GET.getlist('genre[]')
        
        
        if search_term:
            results=results.filter(title__icontains=search_term)
        if selected_genres and '' not in selected_genres:
            selected_genres=[int(g) for g in selected_genres]
            for genid in selected_genres:
                results = results.filter(genre=genid)   
        if results.exists():
            paginator=Paginator(results,4)
            page_number=request.GET.get('page',1)
            page_obj=paginator.get_page(page_number)
            context={"page_obj":page_obj, "genres": genre, "search":search_term,
    "selected_genre": selected_genres }
            return render(request,'search_results.html',context)
        else:
            return redirect('movie_list')
    if not results.exists():
        results=None
        messages.error(request,"Not movies is found")
        
    messages.error(request,"please enter a valid name")      
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
    pic=UserProfile.objects.get(user=usr)

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
    
    context={'usrpro':prof,'count':moviecount,'watchlistcount':watchlistcont,'movie':lis,'reviews':list , "pict":pic}
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
        bio = request.POST.get('bio')
        profile_picture = request.FILES.get('profile_picture')
        has_error=False
        
        if not username:
            messages.error(request,"Enter valid username")
            has_error=True 
        if not firstname:
            messages.error(request,"Enter valid firstname")
            has_error=True   
        if not lastname:
            messages.error(request,"Enter valid lastname")
            has_error=True
        if not email:
            messages.error(request,"Enter valid email")
            has_error=True  
        else:
            try:
                EmailValidator()(email) 
            except ValidationError:
                 messages.error(request, "Invalid email format.")
                 has_error=True                       
        
        if has_error:
            return redirect('profile')
        
        try:
            user.username=username
            user.first_name=firstname
            user.last_name=lastname
            user.email=email
            user.save()

            profile, created = UserProfile.objects.get_or_create(user=user)
            profile.bio = bio
            if profile_picture:
                profile.profile_picture = profile_picture  # Only update if user selected a new image
            profile.save()
            return redirect('userlogin')
        except Exception as e:
                 messages.error(request,"already exist")

       

    return redirect('profile')    
       


#function for reactions

def reaction(request,rid):
    reid=rid
    if request.method=='POST':
        mid=request.POST.get('movieid')
        reaction_type=request.POST.get('reactiontype')

        if reaction_type not in ['like','dislike']:
            messages.error(request,"invalid reaction")
        exisiting_reaction= Reaction.objects.filter(userid=request.user,reviewid=reid).first()     

        try:
            review=ReviewRating.objects.get(reviewid=reid) 
        except Exception as e:
            messages.error(request,"Review not found")
      

        if exisiting_reaction:
            if exisiting_reaction.reactiontype==reaction_type:
                exisiting_reaction.delete()
                messages.info(request,"Reaction is deleted")

            else:
                exisiting_reaction.reactiontype=reaction_type
                exisiting_reaction.save()
                messages.info(request, "Reaction updated")
        else:
            Reaction.objects.create(userid=request.user,reviewid=review,reactiontype=reaction_type)
            messages.info(request, "Reaction added")
    user_reaction = None
    if request.user.is_authenticated:
        existing_reaction = Reaction.objects.filter(userid=request.user, reviewid=rid).first()
        if existing_reaction:
            user_reaction = existing_reaction.reactiontype
    
        
    return redirect('information',mid)





    

    
        




             
    
   
