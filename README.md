# Green Harvest Bistro

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Table of Contents
-  [User Experience](#user-experience)
    - [Project Goals](#project-goals)
    - [User Stories](#user-stories)
    - [Colours Used](#colours-used)
    - [Fonts used](#fonts-used)
  - [Features](#features)
    - [General Features](#general-features)
    - [Database Design](#database-design) 
  - [Frameworks and Programs Used](#frameworks-and-programs-used)
    - [Languages used](#languages-used)
  - [Testing](#testing)
    - [Validator Testing](#validator-testing)
      - [Validation Errors](#validation-errors)
    - [Accessibility](#accessibility)
      - [1. Semantic HTML](#2-semantic-html)
      - [2. Responsive Design](#6-responsive-design)
    - [Manual testing](#manual-testing)
  - [Bugs](#bugs)
  - [Finished Product](#finished-product)
  - [Deployment](#deployment)


Please find the link to my heroku site [here](https://veggie-restaurant-pp4-ce120585246e.herokuapp.com/)

## Project Goals
The goal of this project is to create an engaging and user-friendly online platform for a vegetarian restaurant, Green Harvest Bistro. The site aims to provide a seamless experience for users looking to explore the restaurant's menu, make reservations, and learn more about the restaurant's philosophy. Additionally, the project focuses on delivering a visually appealing design that reflects the restaurant's commitment to fresh, sustainable, and healthy eating.

## User Stories
As a first-time visitor, I want to easily navigate the website, so that I can quickly find the menu and learn more about the restaurant.
As a returning customer, I want to log in and view my past reservations, so that I can easily manage my bookings.
As a health-conscious diner, I want to explore a variety of vegetarian and vegan dishes, so that I can choose a meal that fits my dietary preferences.
As a user interested in booking a table, I want to easily find and use the booking form, so that I can reserve a table quickly.
As a site owner, I want to manage reservations and view customer feedback, so that I can improve the dining experience.

## Colours Used
The color scheme of the site was carefully chosen to reflect the natural and organic theme of Green Harvest Bistro. The primary colors used are:

Green (#4CAF50): Represents nature, health, and sustainability. It is used for headings, buttons, and highlights.
White (#FFFFFF): Provides a clean and minimal background, making content easy to read.
Dark Green (#2c5f2d): Used for text and menu links, creating a contrast with the white background.
Light Gray (#f4f4f4): Used as a subtle background color for sections and forms, adding depth without overwhelming the user.

## Fonts Used
The typography of the website was selected to enhance readability and maintain a professional yet inviting look. The primary fonts used are:

Arial: A clean and widely supported sans-serif font, chosen for its simplicity and readability across all devices.
Sans-serif: Used as the fallback font to ensure consistency in case Arial is not available.
These fonts were selected to provide a modern and approachable feel, aligning with the brand's identity of being fresh, natural, and accessible.

## General Features

### Home Page
Overview: The home page provides a welcoming introduction to Green Harvest Bistro, highlighting the restaurant's focus on vegetarian and plant-based cuisine.
Navigation Links: The page includes easy-to-use navigation links to other sections of the site, such as the Menu, Booking page, and Login/Signup pages.
Call to Action: Encourages users to explore the menu or make a reservation if they are logged in. If not logged in, prompts users to sign up or log in to access booking features.
### Menu Page
Detailed Menu Display: This page features a comprehensive list of the restaurant's dishes, organized by category (e.g., starters, mains, desserts).
Special Dietary Information: The menu highlights dishes that cater to specific dietary requirements, such as vegan or gluten-free options.
### Booking Page
User Bookings Section: Logged-in users can view their current and past bookings, including details like date, time, number of guests, and any special requests.
Booking Form: Allows users to make a new reservation by filling out a form with their details, including date, time, and number of guests. The form is only accessible to logged-in users.
### Login Page
User Login: Provides a form for existing users to log in to their accounts.
Redirects: After successful login, users are redirected to the booking page or their previous location.
### Signup Page
New User Registration: Allows new users to create an account by providing a username, email, and password.
Post-Registration Redirect: After signing up, users are automatically logged in and redirected to the booking page.
### Logout Page
Confirmation: Informs users that they have successfully logged out.
Navigation: Includes a link or button to return to the home page.
These descriptions highlight the key features of each page on your rest

### Frameworks and Programs used

- [Git](https://git-scm.com)  
   Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.  
- [GitHub](https://github.com)  
   GitHub was used to store the projects code after being pushed from Git. 
- [Heroku](https://www.heroku.com)   
   Heroku was used to deploy the website.  


## Database Design

### Booking Model
The Booking model captures all the necessary details related to a reservation at the Green Harvest Bistro. This model includes the following fields:

- user (ForeignKey): A reference to the User model, representing the user who made the booking. This field creates a one-to-many relationship, where a user can have multiple bookings.

- name (CharField): Stores the name of the person making the booking. This is a required field, with a maximum length of 100 characters.

- email (EmailField): Contains the email address of the person making the booking. It ensures that a valid email format is used.

- phone_number (CharField): Holds the phone number of the person making the booking. This is a required field, typically used for contact purposes.

- date (DateField): The date for which the booking is made. This field is essential for scheduling the reservation.

- time (TimeField): The time for the booking, ensuring that the restaurant can manage reservations effectively throughout the day.

- number_of_guests (IntegerField): Represents the number of guests included in the booking. This helps the restaurant prepare for the right number of customers.

- special_requests (TextField, optional): An optional field where users can specify any special requests or preferences for their booking, such as dietary restrictions or seating preferences.

- created_at (DateTimeField, auto_now_add=True): Automatically records the date and time when the booking was created. This helps in tracking and managing bookings over time.

### Functionality of the Booking Model
- User Authentication: The model is tied to the User model, meaning that only authenticated users can make and view bookings. This ensures that the booking process is secure and personalized.

- Form Handling: Forms in the website are linked to this model to handle the input of booking data. The data is validated, saved to the database, and then displayed to the user as a confirmation.

- Querying and Display: The model's data is used to display a list of bookings to the user, showing details such as the date, time, and number of guests. It also allows users to review and manage their reservations.

- This model was designed to be simple yet powerful enough to handle all the necessary aspects of the booking process, ensuring a smooth experience for both the users and the restaurant staff.



## Manual Testing

| **Test Case**                        | **Action**                                              | **Expected Result**                                      | **Actual Result**                                        | **Status** |
|--------------------------------------|---------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|------------|
| **Home Page Load**                   | Navigate to the home page.                              | The home page should load without errors.                 | Home page loads correctly without errors.                 | Pass       |
| **Navigation Bar Links**             | Click on each navigation link (Home, Menu, Booking).    | Each link should take the user to the correct page.       | All links direct the user to the correct page.            | Pass       |
| **User Sign Up**                     | Fill in the sign-up form with valid data and submit.    | User should be redirected to the login page.              | User redirected to login page as expected.                | Pass       |
| **User Login**                       | Log in with valid credentials.                          | User should be redirected to the booking page.            | User redirected to the booking page as expected.          | Pass       |
| **Booking a Table**                  | Fill in the booking form with valid data and submit.    | Booking should be saved and displayed in the bookings list.| Booking saved and displayed correctly in the list.       | Pass       |
| **Logout Functionality**             | Click the logout link.                                  | User should be logged out and redirected to the home page.| User logged out and redirected to home page.              | Pass       |
| **Access Booking Page (Unauthenticated)** | Try to access the booking page without logging in.      | User should be redirected to the login page.              | User redirected to login page as expected.                | Pass       |
| **Invalid Login Attempt**            | Attempt to log in with incorrect credentials.           | User should see an error message and remain on the login page. | Error message displayed, user remains on login page.   | Pass       |
| **Form Validation (Sign Up)**        | Submit the sign-up form with missing or invalid data.   | Form should not submit, and relevant error messages should display. | Form does not submit, error messages displayed. | Pass       |
| **Form Validation (Booking)**        | Submit the booking form with missing or invalid data.   | Form should not submit, and relevant error messages should display. | Form does not submit, error messages displayed. | Pass       |


## Bugs

One of the biggest challenges I faced during this project was the recurring Server Error 500. This error, which generally means something went wrong on the server, became a major headache. Even after carefully going through my code, checking configurations, and verifying all dependencies, I couldn’t quite pin down the exact cause of the problem.

- What Happened:

The error kept showing up whenever I tried to access the home page after deploying the project on Heroku.
The logs from Heroku hinted that something was off, but they didn’t give me enough details to figure out what exactly was wrong.
What I Tried:

- Checking Dependencies: 

I made sure that all the necessary packages in requirements.txt, like gunicorn, Django, and whitenoise, were installed correctly.
Static Files Setup: I spent a lot of time configuring static files with WhiteNoise, thinking that might be the issue. But even after doing that, the error

## Finished Product

Please find the link to my heroku site [here](https://veggie-restaurant-pp4-ce120585246e.herokuapp.com/)

## credits

- [W3Schools](https://www.w3schools.com/) was referenced throughout the project.
- [Stack overflow](https://stackoverflow.com/) was referenced throughout the project.
- For README.md file, reference from my first project was considered.