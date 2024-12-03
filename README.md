# Weather App

### INF601 - Advanced Programming in Python
### Sokly Hour
### Final Project

## Project Overview

This project is part of the **INF601 - Advanced Programming in Python** course, focusing on creating a web application that interacts with the OpenWeather API to fetch and display weather data. The application allows users to search for weather information by location, save the weather data in a database, and delete weather entries. The Weather App is a web application built using Django that allows users to search for weather information, view weather data for different locations, and manage their weather entries. Key features of the application include:

**User Authentication**: Only logged-in users can interact with the app. Users can log in, search for weather data, and manage their weather entries.

**Weather Search**: Users can search for the current weather in a specific location. The app fetches weather data from the OpenWeather API, displaying key information such as temperature, humidity, and description.

**Weather Data Management**: Users can add weather data for their favorite locations, and delete entries they no longer need.

**Responsive Design**: The app is designed using Bootstrap to ensure a seamless and user-friendly experience across various devices. The visually appealing interface makes it easy to search and manage weather data.

**SQLite Database**: The app stores weather data and user information in a SQLite database, ensuring efficient data management. Weather entries are linked to users and saved for later viewing.

**Multi-page Application**: The app includes several pages, including a home page for weather search, register page, login page, logout page, about page and a contact page for user inquiries.

## Features

- **Home Page**: Users can search for the weather in a specific location. The weather data is fetched from the OpenWeather API and displayed on the page.
- **Weather Data**: Displays the weather data for a location, including temperature, humidity, and description.
- **Weather Search**: Users can search for weather information by entering a location, which is then stored in the database.
- **Weather Deletion**: Logged-in users can delete weather entries that they have added.
- **Contact Form**: Users can submit a contact form to send inquiries or feedback.
- **User Authentication**: Only logged-in users can interact with the weather data (add or delete entries).

## Technologies Used

- **Python**: The main programming language used to build the backend logic.
- **Django**: The web framework used for building the application.
- **Django Crispy Forms**: Used to improve the styling and rendering of forms, providing a cleaner and more user-friendly form design with minimal effort.
- **HTML/CSS**: Used to design the user interface of the website.
- **Bootstrap**: Utilized to ensure the application is responsive and mobile-friendly, enhancing the user interface with a clean, modern design.
- **JavaScript**: Used to enhance the user experience.
- **SQLite**: The database used to store weather data.
- **OpenWeather API**: An external API used to fetch weather data for a given location.
- **Django Messages**: To display notifications and error messages to the user.
- **Django Authentication**: For user login and access control.
 

## Setup

### Prerequisites

1. Ensure Python is installed on your system.
2. **Django**: You can install Django by running:
   ```bash
   pip install django

## Getting Started

The running environment and all dependencies can be obtained through the command console in the Python IDE of your choosing.

### Step 1: Pip install requirements.txt
Before getting started, you will need to install this application's dependencies.

In a terminal window, please type the following:
```bash
pip install -r requirements.txt
```
### Step 2: Create SQL entries needed for the database

The SQLite database is not yet in the project, you will need to generate a migration to tell Django which model variables need to be added to the database.

In a terminal window, please type the following:
```bash
python manage.py makemigrations
```

### Step 3: Apply the migrations to the SQL database
Now, you need to apply those migrations to the project.

In a terminal window, please type the following:
```bash
python manage.py migrate 
```

### Step 4: Create a super user
Before you start using the program, you will need to generate a superuser account so that you can add users through the admin interface.

In a terminal window, please type the following:
```bash
python manage.py createsuperuser 
```

### Step 5: Start the server
Now, you will need to start the development server that will be hosting this webapp.

In a terminal window, please type the following:
```bash
python manage.py runserver
```

### Step 6: Navigate to the site
You're ready to view the website. The console should have a link to the server but if not, In your browser's URL bar, please type the following:
```bash
http://localhost:8000
```

## Authors

Contributors names and contact info

SoklyHour
[@SoklyHour](https://www.linkedin.com/in/soklyhour/)


## Acknowledgments
Inspiration, code snippets, etc.
* [django](https://docs.djangoproject.com/en/5.1/intro/)
* [bootstrap](https://getbootstrap.com/)
* [w3schools](https://www.w3schools.com/django/)
* [ChatGPT](https://chatgpt.com/share/674e5c16-4e58-8005-9778-23fc9f076f07)