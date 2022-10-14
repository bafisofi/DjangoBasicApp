from multiprocessing import managers
from platform import release
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Genre(models.Model):
  name = models.CharField(max_length=64, help_text="Genre of the movie")

  def __str__(self):
      return self.name

class Director(models.Model):
  first_name= models.CharField('First Name', max_length=120)
  last_name= models.CharField('Second Name', max_length=120)
  date_of_birth= models.DateField(null=True, blank=True)
  date_of_death= models.DateField('Died',null=True, blank=True)
  place_of_birth= models.CharField(max_length=120)
  place_of_death= models.CharField(max_length=120,null=True, blank=True)
  biography=models.TextField(blank=True)

  def __str__(self):
    return '%s (%s)' % (self.last_name, self.first_name)      

class Movie(models.Model):
   title_movie = models.CharField(max_length=32)
   director= models.ForeignKey(Director, on_delete=models.SET_NULL, null=True)
   summary= models.TextField(blank=True)
   release_date=models.DateField(null=True, blank=True)
   genre=models.ManyToManyField(Genre)
   movie_image=models.ImageField(null=True, blank=True, upload_to="images/")


   def __str__(self):
      return self.title_movie


class Venue(models.Model):
  name= models.CharField('Venue Name', max_length=120)
  address=models.CharField(max_length=300)
  zip_code=models.CharField('Zip Code', max_length=15)
  phone=models.CharField('Contact phone', max_length=25, blank=True)
  web=models.URLField('Website Address', max_length=120)
  email_address= models.EmailField('Email Address', blank=True)

  def __str__(self):
    return self.name


class ClubUser(models.Model):
  first_name= models.CharField('First Name', max_length=120)
  last_name= models.CharField('Second Name', max_length=120)
  email= models.EmailField('Email Addres')

  def __str__(self):
    return self.first_name + ' '+ self.last_name

class Cinema(models.Model):
  name= models.CharField('Event Name', max_length=120)
  movie_title=models.ForeignKey(Movie, blank=True, null=True, on_delete=models.SET_NULL)
  director=models.ForeignKey(Director, blank=True, null=True, on_delete=models.SET_NULL)
  event_date=models.DateTimeField(blank = True, null=True)
  venue = models.ForeignKey(Venue, blank = True, null=True, on_delete=models.SET_NULL)
  #venue= models.CharField(max_length=120)
  description=models.TextField(blank=True)
  manager=models.ForeignKey(User, blank = True, null=True, on_delete=models.SET_NULL)
  attendees=models.ManyToManyField(ClubUser, blank=True)


  def __str__(self):
    return self.name    