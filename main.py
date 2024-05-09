from fastapi import FastAPI
import pandas as pd

app = FastAPI()

recipes = {
    1 : {
    "name": "Good Old Fashioned Pancakes",
    "url": "https://www.allrecipes.com/recipe/21014/good-old-fashioned-pancakes/",
    "category": "breakfast-and-brunch",
    "author": "dakota kelly",
    "summary": "This is a great recipe that I found in my Grandma's recipe book. Judging from the weathered look of this recipe card, this was a family favorite.",
    "rating": 4.56,
    "rating_count": 17098,
    "review_count": 12990,
    "ingredients": "1½ cups all-purpose flour ; 3½ teaspoons baking powder ; 1 teaspoon salt ; 1 tablespoon white sugar ; 1¼ cups milk ; 1  egg ; 3 tablespoons butter, melted",
    "directions": "In a large bowl, sift together the flour, baking powder, salt and sugar. Make a well in the center and pour in the milk, egg and melted butter; mix until smooth. Heat a lightly oiled griddle or frying pan over medium-high heat. Pour or scoop the batter onto the griddle, using approximately 1/4 cup for each pancake. Brown on both sides and serve hot.",
    "prep": "5 mins",
    "cook": "15 mins",
    "total": "20 mins",
    "servings": 8,
    "yield": "8 servings",
    "calories": 158.3,
    "carbohydrates_g": 21.7,
    "sugars_g": 3.5,
    "fat_g": 5.9,
    "saturated_fat_g": 3.4,
    "cholesterol_mg": 37.7,
    "protein_g": 4.5,
    "dietary_fiber_g": 0.6,
    "sodium_mg": 503.6,
    "calories_from_fat": 53.3,
    "calcium_mg": 140.1,
    "iron_mg": 1.4,
    "magnesium_mg": 10.6,
    "potassium_mg": 92.3,
    "zinc_mg": "",
    "phosphorus_mg": "",
    "vitamin_a_iu_IU": 235.6,
    "niacin_equivalents_mg": 2.3,
    "vitamin_b6_mg": "",
    "vitamin_c_mg": 0.1,
    "folate_mcg": 47.9,
    "thiamin_mg": 0.2,
    "riboflavin_mg": "",
    "vitamin_e_iu_IU": "",
    "vitamin_k_mcg": "",
    "biotin_mcg": "",
    "vitamin_b12_mcg": "",
    "mono_fat_g": "",
    "poly_fat_g": "",
    "trans_fatty_acid_g": "",
    "omega_3_fatty_acid_g": "",
    "omega_6_fatty_acid_g": ""
  }
}

@app.get("/")
def home():
    return {"Data": "Home"}

@app.get("/about")
def about():
    return{"Data": "About"}

@app.get("/reccomended")
def get_reccomended():
    #code here
    return 101

@app.get("/get-recipe/{recipe_id}")
def get_recipe(recipe_id: int):
    recipe = recipes[recipe_id]
    name = recipe["title"]
    cookTime = recipe["total"]
    imageURL = recipe["imageURL"]
    return {
            "id": recipe_id,
            "name": name,
            "imageURL": imageURL,
            "cookTime": cookTime
            }

@app.get("/search/{recipe_id}")
def search_recipe(recipe_id: int):
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
