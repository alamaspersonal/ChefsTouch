from fastapi import FastAPI
import pandas as pd
import recipe

app = FastAPI()

recipes = recipe.read_json_file("RecipesCleaned.json")
maxRecipes = len(recipes) - 1

@app.get("/")
def home():
    return {"Data": "Home"}

@app.get("/about")
def about():
    return{"Data": "About"}

@app.get("/get-recipe/{recipe_id}")
def get_recipe(recipe_id: int):
    if(recipe_id > maxRecipes or recipe_id < 0):
        return 400
    return recipe.get_recipe(recipes[recipe_id], recipe_id)

@app.get("/recommended")
def get_recommended():
    recipe_list = recipe.recommend(recipes)
    if(recipe_list):
        return recipe_list
    return 400

@app.get("/few-ingredients")
def get_few_ingredients():
    recipe_list = recipe.few_ingredients(recipes)
    if(recipe_list):
        return recipe_list
    return 400

@app.get("/search/{recipe_id}")
def search_recipe(recipe_id: int):
    if recipe_id > maxRecipes or recipe_id < 0:
        return 400
    return recipes[recipe_id]

#@app.post("/create-item/{recipe_id}")
#def create_recipe(recipe_id, recipe: Recipe):
#    if(recipe in recipes):
#        return 0
#    recipes[recipe_id] = {"title": recipe.title, "directions": recipe.directions, 
#                          "ingredients": recipe.ingredients, "language": recipe.language,
#                          "source": recipe.source, "tags": recipe.tags, "url": recipe.url}
    

@app.put("/put-recipe/{recipe_id}/{name}")
def put_recipe(recipe_id: int, name: str):
    #code here
    return 201
