"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Import necessary modules from Django
from django.contrib import admin  # To access Django's admin interface
from django.urls import path, include  # For URL routing and including other apps' URL configurations
from users import views as user_views  # Import the views from the 'users' app and alias as user_views
from django.contrib.auth import views as auth_views  # Import the authentication views for login/logout

# URL patterns for routing requests
urlpatterns = [
    # Include the URLs from the weatherApp app (defined in 'weatherApp.urls')
    path('', include('weatherApp.urls')), 
    
    # Admin interface URL
    path('admin/', admin.site.urls),  # Path for accessing the Django admin site
    
    # URL for user registration (using the 'register' view from the 'users' app)
    path("register/", user_views.register, name="user-register"),
    
    # URL for user login (using Django's built-in LoginView)
    path("login/", auth_views.LoginView.as_view(template_name="users/login.html"), name="user-login"),
    
    # URL for user logout (using Django's built-in LogoutView)
    path("logout/", auth_views.LogoutView.as_view(template_name="users/logout.html"), name="user-logout"),
    
    # URL for the user profile page (using the 'profile' view from the 'users' app)
    path("profile/", user_views.profile, name="user-profile"),
]
