from pickle import FALSE
from re import M
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Cinema, Venue, Movie, Director
from .forms import VenueForm, CinemaForm, MovieForm, DirectorForm

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

from django.core.paginator import Paginator


def cinema_pdf(request):
	
	buf = io.BytesIO()
	c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
	
	textob = c.beginText()
	textob.setTextOrigin(inch, inch)
	textob.setFont("Helvetica", 14)

	
	
	cinemas = Cinema.objects.all()
   

   
	lines = []

	for cinema in cinemas:
		lines.append("Name Event: " + cinema.name)
		lines.append("Date Event: " + str(cinema.event_date))
		lines.append("Venue Event: " + str(cinema.venue))
		lines.append("Movie Name: " + str(cinema.movie_title))
		lines.append("Description: " + cinema.description)
		lines.append("Person in Charge: " + str(cinema.manager))
		lines.append(" ")

	
	for line in lines:
		textob.textLine(line)

	
	c.drawText(textob)
	c.showPage()
	c.save()
	buf.seek(0)

	
	return FileResponse(buf, as_attachment=True, filename='cinema_list.pdf')

  
def add_director(request):
   submitted=False
   if request.method =="POST":
      form =DirectorForm(request.POST)
      if form.is_valid():
         form.save()
         return HttpResponseRedirect('/add_director?submitted=True')
   else:      
      form =DirectorForm
      if 'submitted' in request.GET:
         submitted =True
   return render(request, 'movies/add_director.html',{'form':form, 'submitted':submitted})


def delete_cinema(request, cinema_id):
   cinema = Cinema.objects.get(pk=cinema_id)
   cinema.delete()
   return redirect('list-cinema')

def delete_venue(request, venue_id):
   venue = Venue.objects.get(pk=venue_id)
   venue.delete()
   return redirect('list-venues')

def delete_movie(request, movie_id):
   movie = Movie.objects.get(pk=movie_id)
   movie.delete()
   return redirect('list-movies') 

def delete_director(request, director_id):
   director = Director.objects.get(pk=director_id)
   director.delete()
   return redirect('list-directors')     

def add_cinema(request):
   submitted=False
   if request.method =="POST":
      form =CinemaForm(request.POST)
      if form.is_valid():
         form.save()
         return HttpResponseRedirect('/add_cinema?submitted=True')
   else:      
      form =CinemaForm
      if 'submitted' in request.GET:
         submitted =True
   return render(request, 'movies/add_cinema.html',{'form':form, 'submitted':submitted})

def add_movie(request):
   submitted=False
   if request.method =="POST":
      form =MovieForm(request.POST, request.FILES)
      if form.is_valid():
         form.save()
         return HttpResponseRedirect('/add_movie?submitted=True')
   else:      
      form =MovieForm
      if 'submitted' in request.GET:
         submitted =True
   return render(request, 'movies/add_movie.html',{'form':form, 'submitted':submitted}) 

def update_director(request, director_id):
   director = Director.objects.get(pk=director_id)
   form = DirectorForm(request.POST or None, instance=director)
   if form.is_valid():
      form.save()
      return redirect('list-directors')

   return render(request, 'movies/update_director.html',
    {'director':director,
    'form': form})     

def update_cinema(request, cinema_id):
   cinema = Cinema.objects.get(pk=cinema_id)
   form = CinemaForm(request.POST or None, instance=cinema)
   if form.is_valid():
      form.save()
      return redirect('list-cinema')

   return render(request, 'movies/update_cinema.html',
    {'cinema':cinema,
    'form': form})

def list_directors(request):
   director_list = Director.objects.all()
   p = Paginator(Director.objects.all(), 25)
   page = request.GET.get('page')
   directors = p.get_page(page)
   nums="a" * directors.paginator.num_pages
   return render(request, 'movies/director.html',
    {'director_list':director_list,
    'directors':directors,
    'nums':nums})        
   
def show_director(request, director_id):
   director = Director.objects.get(pk=director_id)
   return render(request, 'movies/show_director.html',
    {'director':director})

def list_venues(request):
   venue_list = Venue.objects.all()
   p = Paginator(Venue.objects.all(), 25)
   page = request.GET.get('page')
   venues = p.get_page(page)
   nums="a" * venues.paginator.num_pages
   return render(request, 'movies/venue.html',
    {'venue_list':venue_list,
    'venues':venues,
    'nums':nums})    
   
def show_venue(request, venue_id):
   venue = Venue.objects.get(pk=venue_id)
   return render(request, 'movies/show_venue.html',
    {'venue':venue})

def list_movies(request):
   movie_list = Movie.objects.all()

   p = Paginator(Movie.objects.all(), 25)
   page = request.GET.get('page')
   movies = p.get_page(page)
   nums="a" * movies.paginator.num_pages


   return render(request, 'movies/movie.html',
    {'movie_list':movie_list,
    'movies':movies,
    'nums':nums})    
   
def show_movie(request, movie_id):
   movie = Movie.objects.get(pk=movie_id)
   return render(request, 'movies/show_movie.html',
    {'movie':movie})

def update_venue(request, venue_id):
   venue = Venue.objects.get(pk=venue_id)
   form = VenueForm(request.POST or None, instance=venue)
   if form.is_valid():
      form.save()
      return redirect('list-venues')

   return render(request, 'movies/update_venue.html',
    {'venue':venue,
    'form': form})

def update_movie(request, movie_id):
   movie = Movie.objects.get(pk=movie_id)
   form = MovieForm(request.POST or None, request.FILES or None, instance=movie)
   if form.is_valid():
      form.save()
      return redirect('list-movies')

   return render(request, 'movies/update_movie.html',
    {'movie':movie,
    'form': form})

def search_venues(request):
   if request.method =="POST":
      searched = request.POST['searched']
      venues = Venue.objects.filter(name__contains=searched)
      return render(request, 
     'movies/search_venues.html',
     {'searched':searched,
     'venues':venues})
   else:
      return render(request, 
     'movies/search_venues.html',
    {})  


def add_venue(request):
   submitted=False
   if request.method =="POST":
      form =VenueForm(request.POST)
      if form.is_valid():
         form.save()
         return HttpResponseRedirect('/add_venue?submitted=True')
   else:      
      form =VenueForm
      if 'submitted' in request.GET:
         submitted =True
   return render(request, 'movies/add_venue.html',{'form':form, 'submitted':submitted})
   


def all_cinema(request):
   # cinema_list = Cinema.objects.all().order_by('event_date')
   cinema_list = Cinema.objects.all()
   p = Paginator(Cinema.objects.all(), 25)
   page = request.GET.get('page')
   cinemas = p.get_page(page)
   nums="a" * cinemas.paginator.num_pages
   return render(request, 'movies/cinema_list.html',
    {'cinema_list':cinema_list,
    'cinemas':cinemas,
    'nums':nums})    


# Create your views here.
def home(request,year=datetime.now().year,month=datetime.now().strftime('%B')):
  month= month.capitalize()
  month_number = list(calendar.month_name).index(month)
  month_number = int(month_number)
  

  cal= HTMLCalendar().formatmonth(
     year,
     month_number)


  now =datetime.now()
  current_year=now.year 

  time=now.strftime('%I:%M:%p') 
  
  event_list =Cinema.objects.filter(
    event_date__year=year,
    event_date__month = month_number
  )
  return render(request, 'movies/home.html', {
     "year":year,
     "month":month,
     "month_number":month_number,
     "cal":cal,
     "current_year":current_year,
     "time":time,
     "event_list":event_list,
  })
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  







































  





























  
  
  
  
  







