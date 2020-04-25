import os
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'cook_book'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tdr956P@myfirstcluster-v3wwf.mongodb.net/cook_book?retryWrites=true&w=majority'

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


@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipe = mongo.db.recipe
    recipe.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    one_recipe = mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)})
    return render_template('editrecipe.html', recipes=one_recipe)


"""@app.route('/delete_recipe/<recipe_id>', methods=['GET'])
def delete_recipe(recipe_id):
    mongo.db.recipe.remove({"_id": ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))"""


if __name__ == '__main__':

    app.run(host='0.0.0.0',

            port=int(os.environ.get('PORT', 5000)),

            debug=True)
