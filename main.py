from fastapi import FastAPI

app = FastAPI()

recipes = {
    1: {
        "title": "World's Best Lasagna",
        "imageURL": "https://www.allrecipes.com/thmb/iOfxQGOJTdM0K6edW-MFkn-nydE=/0x512/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/23600-worlds-best-lasagna-DDMFS-4x3-1196-24c5401652934ffb96d3d94bc9fbe2d7.jpg",
        "url": "https://www.allrecipes.com/recipe/23600/worlds-best-lasagna/",
        "category": "world-cuisine",
        "author": "John Chandler",
        "summary": "It takes a little work, but it is worth it.",
        "rating": 4.8,
        "rating_count": 19358,	
        "review_count": 13217,	
        "ingredients": [
                        "1 pound sweet Italian sausage", "¾ pound lean ground beef",
                        "½ cup minced onion", "2 cloves garlic, crushed", "1 (28 ounce) can crushed tomatoes"
                        "2 (6 ounce) cans tomato paste", "2 (6.5 ounce) cans canned tomato sauce", "½ cup water",
                        "2 tablespoons white sugar", "1½ teaspoons dried basil leaves", "½ teaspoon fennel seeds", "1 teaspoon Italian seasoning",
                        "1½ teaspoons salt, divided, or to taste", "¼ teaspoon ground black pepper", "4 tablespoons chopped fresh parsley",
                        "12  lasagna noodles", "16 ounces ricotta cheese", "1  egg", "¾ pound mozzarella cheese, sliced", "¾ cup grated Parmesan cheese"
                        ],	
        "directions":  [
                        "In a Dutch oven, cook sausage, ground beef, onion, and garlic over medium heat until well browned.",
                        "Stir in crushed tomatoes, tomato paste, tomato sauce, and water. Season with sugar, basil, fennel seeds, Italian seasoning, 1 teaspoon salt, pepper, and 2 tablespoons parsley. Simmer, covered, for about 1 1/2 hours, stirring occasionally.",
                        "Bring a large pot of lightly salted water to a boil. Cook lasagna noodles in boiling water for 8 to 10 minutes.",
                        "Drain noodles, and rinse with cold water.  In a mixing bowl, combine ricotta cheese with egg, remaining parsley, and 1/2 teaspoon salt.",
                        "Preheat oven to 375  degrees F (190 degrees C). To assemble, spread 1 1/2 cups of meat sauce in the bottom of a 9x13-inch baking dish.  Arrange 6 noodles lengthwise over meat sauce. Spread with one half of the ricotta cheese mixture. Top with a third of mozzarella cheese slices. Spoon 1 1/2 cups meat sauce over mozzarella, and sprinkle with 1/4 cup Parmesan cheese.  Repeat layers, and top with remaining mozzarella and Parmesan cheese. Cover with foil: to prevent sticking, either spray foil with cooking spray, or make sure the foil does not touch the cheese."
                        "Bake in preheated oven for 25 minutes. Remove foil, and bake an additional 25 minutes.",
                        "Cool for 15 minutes before serving."
        	            ],
        "prep": "30 mins",
        "cook":	"2 hrs 30 mins",
        "total": "3 hrs 15 mins",
        "servings": 12,
        "calories": 448.2,
        "carbohydrates_g":	36.5,								
        "sugars_g": 8.6,
        "fat_g": 21.3,
        "saturated_fat_g": 9.9,
        "cholesterol_mg": 81.8,
        "protein_g": 29.7,
        "dietary_fiber_g": 4.0,
        "sodium_mg": 1400.4,
        "calories_from_fat": 192.1,
        "calcium_mg": 441.8,
        "iron_mg": 4.1,
        "magnesium_mg": 66.8,
        "potassium_mg": 875.7,
        "zinc_mg": 0,
        "phosphorus_mg": 0,
        "vitamin_a_iu_IU": 1453.9,
        "niacin_equivalents_mg": 10.2,
        "vitamin_b6_mg": 0,
        "vitamin_c_mg":	16.8,
        "folate_mcg": 79.5,
        "thiamin_mg": 0.3,
        "riboflavin_mg": 0,
        "vitamin_e_iu_IU": 0,
    	"vitamin_k_mcg": 0,
        "biotin_mcg": 0,
        "vitamin_b12_mcg": 0,
        "mono_fat_g": 0,
        "poly_fat_g": 0,
        "trans_fatty_acid_g": 0,
        "omega_3_fatty_acid_g": 0,
        "omega_6_fatty_acid_g": 0
    }
}

@app.get("/")
def home():
    return {"Data": "Home"}

@app.get("/about")
def about():
    return{"Data": "About"}

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