from django.shortcuts import render, redirect, get_object_or_404  # Importing render to display templates, redirect for page redirects, and get_object_or_404 to fetch objects or return 404 if not found
from django.contrib import messages  # Importing messages to display success/error notifications to users
from django.contrib.auth.decorators import login_required  # Importing login_required decorator to ensure only logged-in users can access certain views
import requests  # Importing the requests library to make HTTP requests to the weather API
from .models import Weather  # Importing the Weather model to interact with the weather data in the database
from django.conf import settings  # Importing settings to access the WEATHER_API_KEY from settings
from django.http import HttpResponse  # Importing HttpResponse to send HTTP responses (e.g., for invalid requests)

# Home page view - Only logged in users can search weather and add data
@login_required
def home(request):
    weather_data = None  # Initialize weather data variable

    if request.method == "POST":  # If form is submitted (POST request)
        location = request.POST.get("location")  # Get the location from the form
        api_key = settings.WEATHER_API_KEY  # Use the API key from settings
        # Send a request to the OpenWeather API for weather data
        response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric')

        if response.status_code == 200:  # Check if the response is successful
            data = response.json()  # Parse the JSON data from the response
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            description = data["weather"][0]['description']

            # Create and save a new Weather instance
            weather = Weather.objects.create(
                location=location,
                temperature=temperature,
                humidity=humidity,  
                description=description,
            )
            weather.save()  # Save the instance to the database
            messages.success(request, f"Weather data for {location} added successfully.")  # Display success message

        else:
            messages.error(request, "Could not retrieve weather data. Please try again.")  # Display error if API call fails

    # Fetch all weather data instances to display on the page
    weather_data = Weather.objects.all()
    return render(request, 'weather.html', {'weather_data': weather_data})  # Render the weather page with the data

# About page view - Renders the About page
def about(request):
    return render(request, 'about.html')

# Contact page view - Renders the Contact page
def contact(request):
    return render(request, 'contact.html')

# Delete weather view - Only logged in users can delete weather entries
@login_required
def delete_weather(request, weather_id):
    # Fetch the weather instance by ID or return 404 if not found
    weather = get_object_or_404(Weather, id=weather_id)

    if request.method == 'POST':  # Ensure it's a POST request for deletion
        weather.delete()  # Delete the weather entry from the database
        messages.success(request, "Weather data deleted successfully.")  # Display success message

    # Redirect to the home page after deletion
    return redirect('home')

# Define the view that handles the contact form submission
def submit_contact(request):
    if request.method == 'POST':  # If the form is submitted (POST request)
        name = request.POST.get('name')  # Get the name from the form

        # Display a success message with the user's name
        messages.success(request, f"Thank you, {name}, for contacting us!")
        # Render a success page with the name
        return render(request, 'contact_success.html', {'name': name})
    else:
        # Return an error response if the request method is not POST (invalid request)
        return HttpResponse("Invalid request.")

# View for weather search and delete functionality
@login_required
def weather_search_delete(request):
    weather_data = None  # Initialize weather data variable
    if request.method == 'POST':  # If form is submitted (POST request)
        location = request.POST.get('location')  # Get the location from the form
        api_key = settings.WEATHER_API_KEY  # Use the API key from settings
        # Send a request to the OpenWeather API for weather data
        response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric')

        if response.status_code == 200:  # Check if the response is successful
            data = response.json()  # Parse the JSON data from the response
            temperature = data['main']['temp']
            description = data['weather'][0]['description']

            # Create and save a new Weather instance with the fetched data
            weather = Weather.objects.create(
                location=location,
                temperature=temperature,
                description=description
            )
            # Fetch all weather data for the given location to display on the page
            weather_data = weather.objects.filter(location=location)
        else:
            messages.error(request, "Weather data not found.")  # Display error if API call fails

    return render(request, {'weather_data': weather_data})  # Render the page with the fetched weather data
