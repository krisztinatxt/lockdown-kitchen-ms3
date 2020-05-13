from flask_pymongo import PyMongo
import os
from os import path
from flask import Flask, render_template, redirect, request, url_for
if path.exists("env.py"):
    import env

app = Flask(__name__)

os.environ.get("MONGO_URI")
os.environ.get("MONGO_DBNAME")


mongo = PyMongo(app)

@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port = int(os.environ.get('PORT')),
    debug=True)