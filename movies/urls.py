from django.urls import path
from . import  views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',views.home, name="home"),
    path('<int:year>/<str:month>/',views.home, name="home"),
    path('cinema', views.all_cinema, name="list-cinema"),
    path('add_cinema', views.add_cinema, name="add-cinema"),
    path('add_movie', views.add_movie, name="add-movie"),
    path('add_director', views.add_director, name="add-director"),
    path('update_cinema/<cinema_id>', views.update_cinema, name='update-cinema'),
    path('add_venue', views.add_venue, name="add-venue"),
    path('list_venues', views.list_venues, name="list-venues"),
    path('show_venue/<venue_id>', views.show_venue, name='show-venue'),
    path('list_movies', views.list_movies, name="list-movies"),
    path('show_movie/<movie_id>', views.show_movie, name='show-movie'),
     path('list_directors', views.list_directors, name="list-directors"),
    path('show_director/<director_id>', views.show_director, name='show-director'),
    path('update_venue/<venue_id>', views.update_venue, name='update-venue'),
    path('update_movie/<movie_id>', views.update_movie, name='update-movie'),
    path('update_director/<director_id>', views.update_director, name='update-director'),
    path('seach_venues', views.search_venues, name="search-venues"),
    path('delete_cinema/<cinema_id>', views.delete_cinema, name='delete-cinema'),
    path('delete_venue/<venue_id>', views.delete_venue, name='delete-venue'),
    path('delete_movie/<movie_id>', views.delete_movie, name='delete-movie'),
    path('delete_director/<director_id>', views.delete_director, name='delete-director'),
    path('cinema_pdf', views.cinema_pdf, name='cinema-pdf'),
    

    
]

urlpatterns += staticfiles_urlpatterns()