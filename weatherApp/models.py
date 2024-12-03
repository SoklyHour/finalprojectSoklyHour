from django.db import models  # Import Django's models module to define the database schema

# Create your models here.

class Weather(models.Model):
    # Define a model called 'Weather' with the following fields

    location = models.CharField(max_length=200)  # 'location' stores the name of the location as a string (max length: 200 characters)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)  # 'temperature' stores the temperature as a decimal with up to 5 digits (2 of which are after the decimal point)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)  # 'humidity' stores the humidity as a decimal with up to 5 digits (2 after the decimal point)
    description = models.TextField()  # 'description' stores a text description of the weather (no maximum length)

    def __str__(self):
        # This method returns the location name when the Weather object is printed or displayed in the admin interface
        return self.location
