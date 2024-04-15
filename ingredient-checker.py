def add_ingredient_100g(name, cals, fat, carbs, protein):
    #creates an ingredient containing its nutrients at 100g
    ingredient = {
        'Name' : name,
        'Total Calories' : cals,
        'Fat' : fat,
        'Carbohydrates' : carbs,
        'Protein' : protein
    }
    return ingredient

def make_recipe(name, *ingredients):
    #creates a recipe out of predefined ingredients and returns its nutrients based on those ingredients
    recipe = {
        'Name' : name,
        'Total Calories' : 0,
        'Fat' : 0,
        'Carbohydrates' : 0,
        'Protein' : 0
    }

    for ingredient, weight in ingredients:
        proportion = weight / 100.0  # Calculate the proportion based on weight
        recipe['Total Calories'] += ingredient['Total Calories'] * proportion
        recipe['Fat'] += ingredient['Fat'] * proportion
        recipe['Carbohydrates'] += ingredient['Carbohydrates'] * proportion
        recipe['Protein'] += ingredient['Protein'] * proportion

    recipe['Total Calories'] = round(recipe['Total Calories'], 1)
    recipe['Fat'] = round(recipe['Fat'], 1)
    recipe['Carbohydrates'] = round(recipe['Carbohydrates'], 1)
    recipe['Protein'] = round(recipe['Protein'], 1)
    
    return recipe

carrot = add_ingredient_100g('Carrot', 41, 0.4, 7.7, 0.5)
potato = add_ingredient_100g("Potato", 92.7, 0.1, 21, 2.5)
chicken_thigh = add_ingredient_100g("Chicken Thighs", 191, 9.5, 0.1, 26.3)

chicken_and_veg = make_recipe('Chicken and Vegetables', (carrot, 200), (potato, 150), (chicken_thigh, 300))
print(chicken_and_veg)