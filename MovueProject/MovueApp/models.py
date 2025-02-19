from django.db import models 
from django.contrib.auth.models import User 
# Create your models here.


class TableMovie(models.Model):
    movieid=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    description=models.TextField(max_length=500)
    releasedate=models.DateField()

class TableGenre(models.Model):
    genreid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)

class MovieGenre(models.Model):  
    id=models.AutoField(primary_key=True)
    movieid=models.ForeignKey(TableMovie,on_delete=models.CASCADE)
    genreid=models.ForeignKey(TableGenre,on_delete=models.CASCADE) 

class Review(models.Model):
    reviewid=models.AutoField(primary_key=True)
    movieid=models.ForeignKey(TableMovie,on_delete=models.CASCADE)
    genreid=models.ForeignKey(TableGenre,on_delete=models.CASCADE)    
    reviewtext=models.TextField(max_length=500)
    timestamp=models.DateTimeField()
    ratingscore=models.PositiveSmallIntegerField()

class Reaction(models.Model):
    reactionid=models.AutoField(primary_key=True)
    userid=models.ForeignKey(User,on_delete=models.CASCADE)
    reviewid=models.ForeignKey(Review,on_delete=models.CASCADE)
    reactiontype=models.TextField()

class Watchtable(models.Model):
    watchid=models.AutoField(primary_key=True)
    userid=models.ForeignKey(User,on_delete=models.CASCADE)  
    movieid=models.ForeignKey(TableMovie,on_delete=models.CASCADE)  
    addeddate=models.DateTimeField()

    
    

