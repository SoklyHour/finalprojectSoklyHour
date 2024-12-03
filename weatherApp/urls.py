from django.urls import path  # Import path from django.urls to define URL routes
from . import views  # Import views from the current directory (views.py) to handle requests

urlpatterns = [
    path('', views.home, name='home'),  # Home page route - Maps to 'home' view, accessible at the root URL '/'
    path('about/', views.about, name='about'),  # About page route - Maps to 'about' view, accessible at '/about/'
    path('contact/', views.contact, name='contact'),  # Contact page route - Maps to 'contact' view, accessible at '/contact/'
    path('submit_contact/', views.submit_contact, name='submit_contact'),  # Contact form submission route - Maps to 'submit_contact' view
    path('weather/', views.weather_search_delete, name='weather-search-delete'),  # Weather search and delete page - Accessible at '/weather/'
    path('weather/delete/<int:weather_id>/', views.delete_weather, name='delete-weather'),  # Delete specific weather entry - Accessible at '/weather/delete/<weather_id>'
]