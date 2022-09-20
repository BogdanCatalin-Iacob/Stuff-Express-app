## Table of Contents
* [Purpose](#Purpose)
* [User Experience Design (UX)](#User-Experience-Design)
  * [User stories](#User-Stories)
    * [First Time Visitor Goals](#First-Time-Visitor-Goals)
    * [Returning Visitor Goals](#Returning-Visitor-Goals)
    * [Frequent User Goals](#Frequent-User-Goals)
    * [Admin Goals](#admin-user-goals)
  * [Structure](#Structure)
  * [Design](#Design)
    * [Colour Scheme](#Colour-Scheme)
    * [Typography](#Typography)
    * [Wireframes](#Wireframes)
    * [Limitations](#Limitations)
* [Features](#Features)
    * [Existing Features](#Existing-Features)
    * [Future Features](#Features-Left-to-Implement)
* [Technologies](#Technologies)
* [Testing](#Testing)
    * [Test Strategy](#Test-Strategy)
      * [Summary](#Summary)
    * [Test Results](#Test-Results)
    * [Testing Issues](#Issues-and-Resolutions-to-issues-found-during-testing)
* [Deployment](#Deployment)
    * [Project creation](#project-creation)
    * [Deploying on Heroku](#deploying-on-heroku)
    * [Locally](Run-Locally)
* [Credits](#Credits)
    * [Code](#Code)
    * [Content](#Content)
    * [Media](#Media)
    * [Acknowledgements](#Acknowledgements)
    * [Comments](#Comments)

## Purpose
This Website was created for the sole purpose of completing the fourth Milestone Project for the Code Institute's Full Stack Developer course. 
It was built using the knowledge gained from the HTML, CSS, JavaScript, Python, Django and SQL modules. A full list of technologies used can be found in the technologies section of this document.

The live website can be found [here]()<br>
![Website Mock Up]()

## User Experience (UX)

-   ### User stories

    -   #### First Time Visitor Goals
     

    -   #### Returning Visitor Goals
      

    -   #### Frequent User Goals
        

    -   #### Admin User Goals
       

-   ### Structure

    

-   ### Design
    -   #### Colour Scheme
        

    -   #### Typography
        - Font used for headings, buttons: 'Inter' with 'Arial' as fallback font in case 'Inter' is not loaded
        - Font used for all other texts: 'Roboto' with 'Helvetica' as fallback in case 'Roboto' is not loaded
       
        
    -   #### Wireframes
       

    - #### Database
        

-   ### Limitations
    

***
## Features
 
-   ### Existing Features

   

-   ### Features Left to Implement

    - Admin user to be able to create users and give the admin privileges
    - Admin user to be able to edit / delete any recipe created by any user
    - Users to be able to upload photos of final product
   
***

## Technologies

* HTML
	* This project uses HTML as the main language used to complete the structure of the Website.
* CSS
	* This project uses custom written CSS to style the Website.
* Django
    * This is used as the main connection between frontend and backend
* Python
    * This is used as the backend of the project
* Postgresql
    * This is used as database for Users and Categories 
* [MongoDB](https://www.mongodb.com/)
    * This is used as database for Recipes details (name, ingrediets, cooking steps, cooking time, preparation time, owner of the recipe)
* [Materialize](https://materializecss.com/)
    * This is used as frontend framework to display the content in an organized way
* [Font Awesome](https://fontawesome.com/)
	* Font awesome Icons are used for the Social media links contained in the Footer section of the website
* [Google Fonts](https://fonts.google.com/)
	* Google fonts are used throughout the project to import the *Spectral* and *Lora* fonts.
* [Gitpod](https://gitpod.io/)
	* Gitpod is the tool used to develop the Website.
* [GitHub](https://github.com/)
	* GithHub is the hosting site used to store the source code for the Website
* [Git](https://git-scm.com/)
	* Git is used as version control software to commit and push code to the GitHub repository where the source code is stored.
* [Heroku](https://dashboard.heroku.com/)
    * Heroku is used to deploy the web app
* [Pixlr](https://pixlr.com/)
	* Pixlr is used to reduce the file sizes of images before being deployed to reduce storage and bandwith.
* [Google Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools)
	* Google chromes built in developer tools are used to inspect page elements and help debug issues with the site layout and test different CSS styles.
* [Coolors](https://coolors.co/)
    * This was used to select color palette. 
* [Techsini](http://techsini.com/multi-mockup/index.php)
    * tecnisih.com Multi Device Website Mockup Generator was used to create the Mock up image in this README.
* [Favicon](https://favicon.io/)
    * This was used to generate the icon on browser's tab.
* PowerPoint
    * This was used to create wireframes
* [Wave Accessibility tool](https://wave.webaim.org/)
    * this was used to test the website for accessibility for impaired persons
* [CSSGradient](https://cssgradient.io/)
    * used to create the gradient color for delivery banner
***

## Testing

-   ### Test Strategy 

    -   #### Summary 

       

        - The live Project can be found [here]().</br>

    -   ### Test Results

    - All Pages were run through the [W3C HTML Validator](https://validator.w3.org/) and showed no errors.<br>
   


    - CSS Stylesheet was run through the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) and showed no errors.<br>
   

    - Js files were run through [JSHint](https://jshint.com/) and showed no errors.<br>
    

    - Python files were run through [Pep8](http://pep8online.com/) and showed no errors.<br>
    

    - Website was tested by running locally and tested on the deployed version on three different browsers:
       
    - Test header's logo to redirect to home.html (on all pages) - worked as expected on all tested browsers

    - Navbar displays: 
      

    - Navbar on mobile: 
       

    - Home page has two images with links:
        

    - Register form:
	   

    - Login form:
	   

    - Log out
        

    - Admin only - Categories page
	  

    -Footer: 
       

### Issues and Resolutions to issues found during testing


    #### Known bugs/errors not fixed
   

***
## Deployment

This project was developed using a [GitPod](https://gitpod.io) workspace. The code was committed to [Git](https://git-scm.com) and pushed to [GitHub](https://github.com) using the terminal.

-   ### Project Creation
The project was started by navigating to the [template](https://github.com/Code-Institute-Org/gitpod-full-template) and clicking 'Use this template'. Under Repository name I input "Food-Fiesta" and checked the Include all branches checkbox. I then navigated to the new [repository](https://github.com/BogdanCatalin-Iacob/Food-Fiesta). I then clicked the Gitpod button to open the project in Gitpod.

 The following commands were used throughout the project:

* git add filename - This command was used to add fils to the staging area before commiting.
* git commit -m *commit message explaining the updates* - This command was used to to commit changes to the local repository.
* git push - This command is used to push all commited changes to the GitHub repository. 

### Deploying on Heroku
To deploy this page to Heroku from its GitHub repository, the following steps were taken:

1. Create the Heroku App:
    - Select "Create new app" in Heroku.
    - Choose a name for your app and select the location.

2. Create a file named "requirements.txt" and a file named "Procfile" with the following CLI commands:
    - pip3 freeze > requirements.txt
    - echo web: python run.py > Procfile

3. Attach the Postgres database:
    - In the Resources tab, under add-ons, type in Postgres and select the Heroku Postgres option.
    - Click "More" dropdown
    - Select "Run console"
    - type: "python3"
    - import db from the project
    - type CLI command: "db.create_all()"
    - exit()

4. Prepare the env and __init__.py file:
  

5. Log in to Heroku using the terminal Heroku login -i.
    - Then run the following command: **heroku git:remote -a your_app_name_here** and replace your_app_name_here with the name of your Heroku app. This will link the app to your Gitpod terminal.
    - After linking your app to your workspace, you can then deploy new versions of the app by running the command **git push heroku main** and your app will be deployed to Heroku.

    - Or under the "Deploy" menu on Heroku, select:
        - Deployment method: Connect Github
        - Search for name of your project on Github
        - Connect
        - Enable automatic deploys

-   ### Run Locally
1. Navigate to the GitHub [Repository:](https://github.com/BogdanCatalin-Iacob/Food-Fiesta)
1. Click the Code drop down menu.
1. Either Download the ZIP file, unpackage locally and open with IDE (This route ends here) OR Copy Git URL from the HTTPS dialogue box.
1. Open your developement editor of choice and open a terminal window in a directory of your choice.
1. Use the 'git clone' command in terminal followed by the copied git URL.
1. A clone of the project will be created locally on your machine.

***
## Credits
-   ### Code
   

-   ### Content
    
    
-   ### Media
    - The image on the home page was taken from [pexels.com](https://www.pexels.com/photo/sale-sign-in-a-miniature-shopping-cart-and-paper-bag-5632398/)
   

-   ### Acknowledgements
    - I'd like to thank my mentor Daisy McGirr for her guidance throughout my project.<br>