# Opening JSON file
import json

def read_json_file(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON in '{filename}'.")
        return None

def get_recipe(recipe, recipe_id):
    return {
            "id": recipe_id,
            "name": recipe["name"],
            "imageURL": recipe["imageurl"],
            "cookTime": recipe["total"]
            }

def recommend(recipes):
    if not recipes:
        return 400
    else:
        recipe_list = []
        for i in range(len(recipes)):
            recipe = recipes[i]
            if(len(recipe["rating"]) > 4.7):
                clean_recipe = {
                    "id": i,
                    "name": recipe["name"],
                    "imageURL": recipe["imageurl"],
                    "cookTime": recipe["total"]
                }
                recipe_list.append(clean_recipe)
    return recipe_list

def few_ingredients(recipes):
    if not recipes:
        return 400
    else:
        recipe_list = []
        for i in range(len(recipes)):
            recipe = recipes[i]
            if(len(recipe["ingredients"]) < 10):
                clean_recipe = {
                    "id": i,
                    "name": recipe["name"],
                    "imageURL": recipe["imageurl"],
                    "cookTime": recipe["total"]
                }
                recipe_list.append(clean_recipe)
    return recipe_list
