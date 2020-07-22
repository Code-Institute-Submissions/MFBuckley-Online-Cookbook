import os

from os import path
if path.exists('env.py'):
    import env

from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo #import pymongo library
from bson.objectid import ObjectId #importing from BSON library

# flask uses import name to know where to look for templates, resources etc
app = Flask(__name__)

# Connect to database
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

# Create instance of PyMongo
mongo = PyMongo(app)

@app.route('/')

# Display all recipes page
@app.route('/get_recipes')
def get_recipes():
    return render_template("all_recipes.html", recipes=mongo.db.recipes.find())

# Display addrecipe.html page
@app.route('/add_recipe')
def add_recipe():
    return render_template("addrecipe.html")

# Post new recipe to database i.e.clicking save button creates new document in recipes collection
@app.route('/new_recipe', methods=['POST'])
def new_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))

# Connect to Update Recipes file
@app.route('/update_recipe')
def update_recipe():
    return render_template("edit.html", categories=mongo.db.categories.find(),
    recipes=mongo.db.recipes.find())


# Save button click after editing recipe. Find one recipe from collection and edit it.
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id: ObjectId(recipe_id)"})
    all_categories = mongo.db.categories.find()
    return render_template('edit.html', recipe=the_recipe, categories=all_categories)

# Change recipe by accessing tasks collection in database via form action
@app.route('/change_recipe/<recipe_id>', methods=["POST"])
def change_recipe(recipe_id):
    recipes = mongo.db.tasks
    recipes.update({'_id': ObjectId(recipe_id)},
    {        
        'category_name': request.form.get('category_name'),
        'title':request.form.get('title'),
        'ingredients': request.form.get('ingredients'),
        'preparation': request.form.get('preparation'),
        'servings': request.form.get('servings'),
        'prep_time': request.form.get('prep_time'),
        'total_cooking_time': request.form.get('total_cooking_time')
    })
    return redirect(url_for('get_recipes'))

#Delete recipe
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.tasks.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))

    

# Set PORT and IP Address
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)