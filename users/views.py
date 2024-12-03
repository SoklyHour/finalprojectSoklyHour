from django.shortcuts import render, redirect  # Import necessary functions for rendering views and redirecting
from django.contrib import messages  # Import Django's messaging framework for showing feedback messages
from django.contrib.auth.decorators import login_required  # Import the login_required decorator to restrict access to authenticated users

from . import forms  # Import the forms module from the current app

# View for user registration
def register(request):
    # Check if the request method is POST, meaning the form is being submitted
    if request.method == "POST":
        form = forms.userRegisterForm(request.POST)  # Create a form instance with the POST data
        # Validate the form (checks if all fields are correct and required data is present)
        if form.is_valid():
            form.save()  # Save the form data to the database (create the user)
            username = form.cleaned_data.get("username")  # Retrieve the username from the cleaned data
            messages.success(request, f"{username}, you're account has been created, please login!")  # Show a success message
            return redirect('user-login')  # Redirect to the login page after successful registration
    else:
        form = forms.userRegisterForm()  # If it's a GET request, initialize an empty form
    
    # Render the registration template with the form
    return render(request, "users/register.html", {'form': form})

# View for user profile - this view requires the user to be logged in
@login_required()  # Restrict this view to logged-in users only
def profile(request):
    # Render the profile template
    return render(request, 'users/profile.html')  # The user profile page
