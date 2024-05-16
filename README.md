# Recipe App Web Application

Live site hosted on Heroku: 
https://tranquil-journey-26821-bbf38fa9f3ee.herokuapp.com/

# Table of Contents
- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [Features](#features)
- [User Goals](#user-goals)
- [Technical Requirements](#technical-requirements)
- [Project Deliverables](#project-deliverables)
- [Deployment on Heroku](#deployment)


## Introduction
This README provides an overview of the Recipe web application developed using the Django framework. The application allows users to create, read, and add recipes, as well as search for recipes based on ingredients, difficulty, and/or title. It includes a user authentication system, an admin panel for data management, and statistical dashboards for data visualization.

## Getting Started
To get started with the Recipe web application, follow these steps:

1.  Clone the repository to your local machine:     
      git clone: https://github.com/Marvel2410/recipy

2. Install the required dependencies:
      pip install -r requirements.txt

3.  Set up the database:
      python manage.py migrate

4. Create a superuser for admin access:
      python manage.py createsuperuser

5. Run the development server:
      python manage.py runserver

## Features
- User authentication, login, and logout
- Recipe search by ingredient
- Automatic rating of recipes by difficulty level
- Error handling for user input
- Detailed recipe view
- SQLite database for user recipes
- Django Admin dashboard for database management
- Statistics and visualizations based on data analysis

## User Goals
Users can create recipes with ingredients, cooking time, and a difficulty parameter. They can also search for recipes by ingredient.

## Technical Requirements
- Python 3.12.3 and Django 5.0.5
- PostgreSQL database (local)
- Well-documented and tested code on GitHub
- Proper error handling and user-friendly messages
- Easy-to-use interface with simple forms and menus

## Project Deliverables
The project is divided into several exercises, each focusing on different aspects of the application development. Check the Project Deliverables section in repo: python-course1 for a detailed breakdown of achievements.

## Deployment
- Install Heroku CLI
- Login to Heroku
- Create a Heroku App
    heroku create
- Add Heroku Remote
- Deploy the App: git push heroku main
- Run Migrations on Heroku
    heroku run python manage.py migrate
- Create a Superuser on Heroku
    heroku run python manage.py createsuperuser


Created by Stephanie Duda: 
https://marvel2410.github.io/SDudaProfile/ 



