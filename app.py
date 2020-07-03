import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo #import pymongo library
from bson.objectid import ObjectId #importing from BSON library

# flask uses import name to know where to look for templates, resources etc
app = Flask(__name__)

# Connect to database
app.config["MONGO_DBNAME"] = 'online_cooking'
app.config["MONGO_URI"] = 'mongodb://username:pw@myfirstcluster-shard-00-00-riwiq.gcp.mongodb.net:27017,myfirstcluster-shard-00-01-riwiq.gcp.mongodb.net:27017,myfirstcluster-shard-00-02-riwiq.gcp.mongodb.net:27017/online_cooking?ssl=true&replicaSet=myFirstCluster-shard-0&authSource=admin&retryWrites=true&w=majority'

# create instance of PyMongo
mongo = PyMongo(app)

@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    return render_template("all_recipes.html", recipes=mongo.db.recipes.find())

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)