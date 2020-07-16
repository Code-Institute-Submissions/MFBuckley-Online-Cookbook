# Online Cookbook

A database of cooking recipes for the Thermomix kitchen appliance that can be read, edited and updated.
Created by the Vorwerk company, a Thermomix is essentially a powerful blender which also cooks, kneads and stirs food mixtures making it a powerful ally in the kitchen.

# UX

1. As a Full Stack Developer I am creating an online cooking database that allows users to Create, Read, Update and Delete cooking recipes for a Thermomix kitchen appliance.

1. As a back-end developer, I am creating a database of recipes so that it can be searched and updated by a user.

1. As a front-end developer I am creating a responsive webpage using Bootstrap4 so that it works well on all screen sizes.

1. As a cook I would like to display images and text to show what the meal looks like, what ingredients are required and how to prepare it.

1. As a cook I want to add, edit and delete recipes to build a collection of my favourite recipes.

# Features

## Existing Features

Simple website layout for better UI. Database does not have the usual database layout as it is meant for people who cook not necessarily data analysts who are used to database software.
Template inheritance via Jinja code from base.html extended to child html files.

## Features Left to Implement

Changing number of servings adjusts amounts of ingredients necessary to make the recipe.

Ingredients and Preparation textareas are limited to 20 rows.

# Technologies used

[HTML5](https://html.spec.whatwg.org/)

HTML5 is a markup language used for structuring and presenting content on the World Wide Web.

[CSS3](https://www.w3.org/Style/CSS/specs.en.html) 

Cascading Style Sheets 3 is a style sheet language used for describing the presentation of a document written in a markup language like HTML5.

[Bootstrap4](https://getbootstrap.com/)

Bootstrap 4 is the most popular HTML, CSS, and JavaScript framework for developing responsive, mobile-first websites. It was first developed by Twitter developers.

[Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) 

JavaScript is a high-level, often just-in-time compiled and multi-paradigm programming language. 
Alongside HTML and CSS, JavaScript is one of the core technologies of the World Wide Web. JavaScript enables interactive web pages and is an essential part of web applications. 
The vast majority of websites use it for client-side page behavior and all major web browsers have a dedicated JavaScript engine to execute it.

[Python3](https://www.python.org/)

Python is an interpreted, high-level, general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant whitespace. 
Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.
Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly, procedural), object-oriented, and functional programming. 

[Flask](https://www.fullstackpython.com/flask.html)

Flask is a lightweight Python framework based around the components Werkzeug, a utility library and the templating language Jinja.
It makes getting started with Python qiuck and easy and can scale to complex projects. Many extensions exist that can be added to make functionality even easier.

[MongoDB](https://www.mongodb.com/)

MongoDB is a cross-platform document-oriented database program. Classified as a NoSQL database program, MongoDB uses JSON-like documents with optional schemas.
MongoDB Atlas is the global cloud database service for modern applications.


# Testing

# Deployment

Deployed using Heroku Git. Installation instructions may be found [here](https://dashboard.heroku.com/apps/online-cooking-flask-mongo/deploy/heroku-git).

* Login to heroku via terminal
    * ``` $ heroku Login```
* Initialise git repository in terminal
    * ``` git init ```
    * ``` git add . ```
    * ``` git commit -m "Commit message" ```
* Remote from git to heroku via terminal
    * ``` heroku git:remote -a heroku app name ```
* Run Heroku app from terminal 
    * ``` heroku ps:scale web=1 ```

# Credits

## Media

Recipes source and [Thermomix](https://thermomix.vorwerk.de/thermomix/tm6/)

## Acknowledgements

This website idea is a project suggestion for the third milestone project in the Fullstack Web Developer course from Code Institute, Dublin Ireland.



