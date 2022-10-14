from django import forms
from django import forms
from django.forms import ModelForm
from .models import Venue
from .models import Cinema
from .models import Movie
from .models import Director

class VenueForm(ModelForm):
  class Meta:
    model= Venue
    fields= ('name','address','zip_code','phone','web','email_address')
    labels ={
      'name':'',
      'address':'',
      'zip_code':'',
      'phone':'',
      'web':'',
      'email_address':'',

    }

    widgets ={
      'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}),
      'address':forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}),
      'zip_code':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Zip Code'}),
      'phone':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone'}),
      'web':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Web Site'}),
      'email_address':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email' }),
    }


class CinemaForm(ModelForm):
  class Meta:
    model= Cinema
    fields= ('name','movie_title','director','event_date','venue','description','manager','attendees')
    labels ={
      'name':'',
      'movie_title':'Movie Name ',
      'director':' Director Movie',
      'event_date':'YYYY-MM-DD HH:MM:SS',
      'venue':'Venue',
      'description':'',
      'manager':'Person in Charge',
      'attendees':'Attendees',
    }

    widgets ={
      'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':' Event Name'}),
      'movie_title':forms.Select(attrs={'class':'form-select form-control','placeholder':'Film Name'}),
      'director': forms.Select(attrs={'class':'form-select form-control', 'placeholder':' Film Director'}),
      'event_date':forms.DateInput(attrs={'class':'form-control', 'placeholder':'Event Date'}),
      'venue':forms.Select(attrs={'class':'form-select form-control',  'placeholder':'Venue '}),
      'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Description' }),
      'manager':forms.Select(attrs={'class':'form-select form-control', 'placeholder':'Person in Charge'}),
      'attendees':forms.SelectMultiple(attrs={'class':'form-select form-control', 'placeholder':'Attendees'}),
      
    }


class MovieForm(ModelForm):
  class Meta:
    model= Movie
    fields= ('title_movie','director','summary','release_date','genre','movie_image')
    labels ={
      'title_movie':'',
      'director':' Director Movie',
      'summary':'',
      'release_date':'YYYY-MM-DD',
      'genre':'Genre',
      'movie_imagee':'',
    }

    widgets ={
      'title_movie':forms.TextInput(attrs={'class':'form-select form-control','placeholder':'Film Name'}),
      'director': forms.Select(attrs={'class':'form-select form-control', }),
      'summary':forms.Textarea(attrs={'class':'form-control','placeholder':'Description' }),
      'release_date':forms.DateInput(attrs={'class':'form-control', }),
      'genre':forms.SelectMultiple(attrs={'class':'form-select form-control', 'placeholder':'Attendees'}),
      
    } 

class CinemaForm(ModelForm):
  class Meta:
    model= Cinema
    fields= ('name','movie_title','director','event_date','venue','description','manager','attendees')
    labels ={
      'name':'',
      'movie_title':'Movie Name ',
      'director':' Director Movie',
      'event_date':'YYYY-MM-DD HH:MM:SS',
      'venue':'Venue',
      'description':'',
      'manager':'Person in Charge',
      'attendees':'Attendees',
    }

    widgets ={
      'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':' Event Name'}),
      'movie_title':forms.Select(attrs={'class':'form-select form-control','placeholder':'Film Name'}),
      'director': forms.Select(attrs={'class':'form-select form-control', 'placeholder':' Film Director'}),
      'event_date':forms.DateInput(attrs={'class':'form-control', 'placeholder':'Event Date'}),
      'venue':forms.Select(attrs={'class':'form-select form-control',  'placeholder':'Venue '}),
      'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Description' }),
      'manager':forms.Select(attrs={'class':'form-select form-control', 'placeholder':'Person in Charge'}),
      'attendees':forms.SelectMultiple(attrs={'class':'form-select form-control', 'placeholder':'Attendees'}),
      
    }


class DirectorForm(ModelForm):
  class Meta:
    model= Director
    fields= ('first_name','last_name','date_of_birth','date_of_death','place_of_birth','place_of_death','biography')
    labels ={
      'first_name':'',
      'last_name':'',
      'date_of_birth':' DYYYY-MM-DD',
      'date_of_death':'YYYY-MM-DD',
      'place_of_birth':'',
      'place_of_death':'',
      'biography':'',
    }

    widgets ={
      'first_name':forms.TextInput(attrs={'class':'form-select form-control','placeholder':'Director First Name'}),
      'last_name':forms.TextInput(attrs={'class':'form-select form-control','placeholder':'Director Last Name'}),
      'date_of_birth':forms.DateInput(attrs={'class':'form-control', }),
      'date_of_death':forms.DateInput(attrs={'class':'form-control', }),
      'place_of_birth':forms.TextInput(attrs={'class':'form-select form-control','placeholder':'Place of Birth'}),
      'place_of_death':forms.TextInput(attrs={'class':'form-select form-control','placeholder':'Place of Death'}),
      'biography':forms.Textarea(attrs={'class':'form-control','placeholder':'Biography' }), 
    }       