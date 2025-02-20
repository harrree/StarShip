from django.db import models 
from django.contrib.auth.models import User 
# Create your models here.

#Model for Movie table
class Movie(models.Model):
    movieid = models.AutoField(primary_key=True) #Auto incrementing primary key for Movie table
    title=models.CharField(max_length=200) #Title of the movie
    description=models.TextField(max_length=500) #Description of the movie
    #=models.ImageField(upload_to='posters/', null=True, blank=True) #Poster of the movie
    releasedate=models.DateField() #Release date of the movie

    def __str__(self):
        return self.title

#Model for Genre table
class Genre(models.Model):
    genreid=models.AutoField(primary_key=True) #Auto incrementing primary key for Genre table
    name=models.CharField(max_length=200, unique=True) #Unique name of the genre
    #movies=models.ManyToManyField(Movie, related_name="movies") #Many to many relationship with Movie table through MovieGenre table

    def __str__(self):
        return self.name

# # MovieGenre join table to establish Many-to-Many relationship between Genre and Movie
# class MovieGenre(models.Model):  
#     id=models.AutoField(primary_key=True)
#     genreid=models.ForeignKey(Genre,on_delete=models.CASCADE) #Foreign key to Genre table
#     movieid=models.ForeignKey(Movie,on_delete=models.CASCADE) #Foreign key to Movie table 


#Model for ReviewRating table
class ReviewRating(models.Model):
    reviewid=models.AutoField(primary_key=True) #Auto incrementing primary key for ReviewRating table
    userid = models.ForeignKey(User, on_delete=models.CASCADE) #Foreign key to User table
    movieid = models.ForeignKey(Movie, on_delete=models.CASCADE) #Foreign key to Movie table
    rating = models.PositiveSmallIntegerField() #Rating of the movie
    review = models.TextField(max_length=500) #Review of the movie
    timestamp = models.DateTimeField() #Timestamp of the review

    def __str__(self):
        return f"{self.userid.username - self.movieid.title}({self.rating}/10)"

#Reaction model to store user reactions to reviews
class Reaction(models.Model):
    reactionid=models.AutoField(primary_key=True) #Auto incrementing primary key for Reaction table
    userid=models.ForeignKey(User,on_delete=models.CASCADE) #Foreign key to User table
    reviewid=models.ForeignKey(ReviewRating,on_delete=models.CASCADE) #Foreign key to ReviewRating table
    reactiontype=models.CharField(max_length=10, choices=[
        ('like', 'Like'),
        ('love', 'Love'),
        ('funny', 'Funny'),
        ('sad', 'Sad')
    ]) #Type of reaction
    timestamp=models.DateTimeField() #Timestamp of the reaction

    def __str__(self):
        return f"{self.userid.username} reacted {self.reactiontype} on {self.reviewid}"

#Model for Watchlist table
class Watchlist(models.Model):
    watchlistid=models.AutoField(primary_key=True) #Auto incrementing primary key for Watchlist table
    userid=models.ForeignKey(User,on_delete=models.CASCADE) #Foreign key to User table
    movieid=models.ForeignKey(Movie,on_delete=models.CASCADE) #Foreign key to Movie table
    added_date=models.DateTimeField() #Timestamp of the movie added to watchlist

    def __str__(self):
        return f"{self.userid.username} added {self.movieid.title} to Watchlist"


    
    

