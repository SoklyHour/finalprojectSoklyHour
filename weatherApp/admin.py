from django.contrib import admin  # Import the Django admin module
from .models import Weather  # Import the Weather model from the current app's models

# Register your models here.
# This registers the Weather model so it can be managed through the Django admin interface.
admin.site.register(Weather)
