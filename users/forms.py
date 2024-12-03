from django import forms  # Django's form handling module
from django.contrib.auth.models import User  # User model from Django's auth system
from django.contrib.auth.forms import UserCreationForm  # Form class for user creation

# Creating a custom form for user registration that inherits from UserCreationForm
class userRegisterForm(UserCreationForm):
    # Adding an additional email field to the registration form
    email = forms.EmailField()

    # Meta class to define the model and the fields to be used in the form
    class Meta:
        model = User  # Specifies that the form will be for the User model
        # Defining the fields that will be used in the form (username, email, password1, and password2)
        fields = ['username', 'email', 'password1', 'password2']
