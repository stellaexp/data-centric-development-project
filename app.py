import os
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'recipes'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tdr956P@myfirstcluster-v3wwf.mongodb.net/recipes?retryWrites=true&w=majority'

app.secret_key = "randomstringneedstobechanged"

mongo = PyMongo(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    """Username entry page"""
    if request.method == "GET":
        session.clear()

    if request.method == "POST":
        session["username"] = request.form["username"]

    if "username" in session:
        username = session['username']
        return render_template("welcome.html", username=username)

    return render_template("index.html")


@app.route('/welcome')
def welcome():
    username = session['username']
    return render_template("welcome.html", username=username)


@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", recipe=mongo.db.recipe.find())


@app.route('/add_recipe')
def add_recipe():
    return render_template("addrecipe.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
