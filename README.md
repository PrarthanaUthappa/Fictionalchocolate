# Chocolate Management System

This project is a Chocolate Management System built using Django. It allows users to manage chocolate products, including adding, updating, and deleting entries, along with handling user authentication and administrative tasks.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Technologies](#technologies)
- [License](#license)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/PrarthanaUthappa/FictionalChocolateApp.git

<!-- Navigate to the project directory: -->
cd chocolateProject

<!-- Set up a virtual environment (recommended): -->
python -m venv env
<!-- on windows -->
env\Scripts\activate 

<!-- Install the dependencies:  -->
Django==4.1

<!-- run migrations -->
python manage.py makemigrations
python manage.py migrate

<!-- start  -->
python manage.py runserver
