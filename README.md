# Data centric Development Milestone Project
My project for Code Institute's Data Centric Development milestone was to create an online recipe book with CRUD functionality, which I aptly named 'Oh Crumbs!'.

## UX
I started the UX process by looking at recipe websites, namely BBC Good Food as it’s a very popular resource for home cooks. I noted what a user expects to see from a recipe, such as preparation, cooking time, amount of people served etc. I then focused on who my target audience was, I decided on ‘plant eaters’, so there would be no meat, fish, dairy or eggs on the site.

My user story goes as follows:

As a plant-based eater, I want to have access to a website that has recipes I can read, contribute to, update and delete if I don’t think they fit the site.

As a site owner, I want to provide a platform for users to read, collaborate and manage a variety of plant-based recipes.

The website should be as intuitive as possible with clear points of interaction. Please find wireframes located in the ‘user research’ folder in the project.

## Database schema

The structure of the data in MongoDB is as follows;

```{
    "_id": {
        "$oid": "objectId"
    },
    "recipe_name": "string",
    "prep_time": {
        "$numberInt": "integer"
    },
    "cook_time": {
        "$numberInt": "integer"
    },
    "serves": {
        "$numberInt": "integer"
    },
    "ingredients": "string",
    "method": "string",
    "allergen_name": "string"
}`

## Features
The main purpose of the project, as set out in the brief, was to demonstrate CRUD functionality.

## Existing Features
* Feature 1 - login - user can 'login' and username is saved for the session.

* Feature 2 - read - access to a directory of recipes that a user can select individually to read.

* Feature 3 - create - add recipe to the database.

* Feature 4 - update - retrieve recipes from db and edit.

* Feature 5 - delete - delete any recipes that aren't suitable. A modal is used to confirm deletion.

## Features Left to Implement
* Authenticated login - the project guidelines stated that authenticated login was not required. However, if this project were to go live to the public, it would definitley require a username and encrypted password to be saved in the db, to be retrieved on each login. 

* Recipe image - each recipe needs to be assigned a relevant image, denoting what the finished recipe looks like. There should be an upload buttton on both the add and edit recipe page, which allows a user to submit their own image.

* Filter/sort functionality - users should be able to filter and sort the recipes based on their preferences.

## Technologies Used
Aside from the standard front-end technologies HTML, CSS and Javascript, this project uses:

1.[Balsamiq](https://balsamiq.com/)
* Used to create low-fidelity wireframes.
2. [Materialize](https://flask.palletsprojects.com/en/1.1.x/)
* Front-end CSS and JS library.
3. [Google Fonts](https://fonts.google.com/)
*  For appealing typography.
4. [jQuery](https://jquery.com/)
*  The project uses JQuery to simplify DOM manipulation.
5. [Python](https://www.python.org/)
*  The backend programming language.
6. [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* Python microframework.
7. [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
* Used for templating and looping.
8. [MongoDB](https://www.mongodb.com/)
* The database to store and retreive recipes from.

## Testing

I decided to manually test the application. Each page was tested on Chrome, Firefox, Safari, Opera, Internet Explorer using the following the testing criteria;

1. Login page
* Form should take a username and a pseudo password field, which does not get saved.
* The username should be stored in a session.
* Link to the about/welcome page.

2. Navigation menu
* Logo in top left corner should link to welcome/about page.
* 'Recipes' redirects to full recipe index.
* 'New' redirects to 'Add recipe'.
* 'Manage' redirects to 'Manage Recipes', which is an overview of all recipes.
* 'Logout' returns user to the login page.

2. About page
* Username should be displayed on 'logging in'.
* Slides should be automatically looping through the carousel.
* Link to recipe index should redirect user to 'Recipes'.

3. Recipe index
* Recipes from the database should be displaying in order of submission.
* Link to recipe working.

4. Add recipe
* Form asks user to validate each field.
* Allergens list displaying correctly from database.
* Form submits correctly.

4. Edit recipe
* Correct recipe retrieved from db for editing.
* Form asks for validation for each field.
* Allergens list displaying correctly from database.
* Form submits correctly.

5. Mange recipes
* All recipes displaying.
* Link to edit button working.
* Modal for final deletion working.

6. Logout
* Ends user session by returning to 'login' page.


The application has also been tested for defensive design on Chrome's responsive viewer, which includes Moto G4, Galaxy S5, Pixel 2, Pixel 2XL iPhone 5/SE, iPhone 6/7/8, iPhone 6/7/8 Plus, iPhone X, iPad, iPad Pro.

## Deployment
This project has been deployed to Heroku and you can find a live demo of the site [here](https://data-centric-development-k.herokuapp.com/).

## Running the application locally
Clone the repository locally via GitHub, cd into the repo and create a virtual environment. Once you're inside the virtual env, run this command;

`pip3 freeze --local > requirements.txt`

To run the application locally use this command

`python3 run.py`

## Credits
I'd like to thank the Tutor Support team at Code Institute who pointed me in the right direction with any issues I became particularly stuck on.

## Content
All recipes were taken from BBC Good Food, or otherwise recollected from memory myself.

## Media
The photos used in this site were obtained from https://unsplash.com/. The favicon was generated by https://favicon.io/favicon-generator/

## Acknowledgements
I received inspiration and recipes details for this project from BBC Good Food https://www.bbcgoodfood.com/. I also looked at a vegetarian recipe and resource website, Anna Jones http://annajones.co.uk/recipes.