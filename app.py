import os
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'cook_book'
app.config["MONGO_URI"] = os.get.environ('COOKBOOK')

app.secret_key = os.get.environ('RANDOMSTRING')

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


@app.route('/about_page')
def about_page():
    return render_template("about.html")


@app.route('/get_recipes')
def get_recipes():
    recipe = mongo.db.recipe.find()
    allergens = mongo.db.allergens.find()
    return render_template("recipes.html", recipe=recipe, allergens=allergens)


@app.route('/recipe_index')
def recipe_index():
    recipe = mongo.db.recipe.find()
    return render_template("recipeindex.html", recipe=recipe)


@app.route('/full_recipe/<recipe_id>')
def full_recipe(recipe_id):
    full_recipe = mongo.db.recipe.find_one({'_id': ObjectId(recipe_id)})
    text = full_recipe['ingredients']
    x = text.split(',')
    next = full_recipe['method']
    y = next.split('.')
    allergens = mongo.db.allergens.find()
    return render_template('fullrecipe.html', full_recipe=full_recipe,
                           ingredients=x, ingredient=y, allergens=allergens)


@app.route('/add_recipe')
def add_recipe():
    return render_template("addrecipe.html",
                           allergens=mongo.db.allergens.find())


@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipe = mongo.db.recipe
    recipe.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    one_recipe = mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)})
    all_allergens = mongo.db.allergens.find()
    return render_template('editrecipe.html', item=one_recipe,
                           allergens=all_allergens)


@app.route('/update_recipe/<recipe_id>', methods=['POST'])
def update_recipe(recipe_id):
    recipe = mongo.db.recipe
    recipe.update_one({'_id': ObjectId(recipe_id)}, {'$set': {
        'recipe_name': request.form['recipe_name'],
        'prep_time': request.form['prep_time'],
        'cook_time': request.form['cook_time'],
        'serves': request.form['serves'],
        'ingredients': request.form['ingredients'],
        'method': request.form['method'],
        'allergen_name':request.form['allergen_name']
        }})
    return redirect(url_for('get_recipes'))


@app.route('/delete_recipe/<recipe_id>', methods=['GET'])
def delete_recipe(recipe_id):
    mongo.db.recipe.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))


if __name__ == '__main__':

    app.run(host='0.0.0.0',

            port=int(os.environ.get('PORT', 5000)),

            debug=True)
