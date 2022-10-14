from django.contrib import admin

# Register your models here.

from .models import Cinema
from .models import ClubUser
from .models import Venue
from .models import Director
from .models import Genre
from .models import Movie


#admin.site.register(Cinema)
admin.site.register(ClubUser)
#admin.site.register(Venue)
admin.site.register(Genre)
admin.site.register(Director)
admin.site.register(Movie)

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
   list_display=('name','address','phone')
   ordering=('name',)
   search_fields= ('name','address')

@admin.register(Cinema) 
class Cinema(admin.ModelAdmin):
  fields=(('name','venue'),'event_date','movie_title','description','manager','attendees')
  list_display=('name','event_date','venue','movie_title')
  list_filter=('event_date','movie_title')
  ordering=('-event_date',)