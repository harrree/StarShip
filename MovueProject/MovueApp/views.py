from django.shortcuts import render,redirect
from .models import Movie


# Create your views here.
def movie_list(request):
    move=Movie.objects.all()
    context={"list":move}
    return render(request,"index.html",context)


def information(request,id):
    
    movi=Movie.objects.filter(movieid=id).values()
    
    context={'key':movi}
    return render(request,'movie_list.html',context)

 