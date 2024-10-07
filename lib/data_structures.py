import math 

spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

# function get_names()
# params: list of spicy_foods 
# returns: list of strings with the names of each spicy food
def get_names(spicy_foods):
    names = [food["name"] for food in spicy_foods]
    return names

# function get_spiciest_foods()
# params: list of spicy_foods
# returns: list of dictionaries where the heat level of the food is > 5
def get_spiciest_foods(spicy_foods):
    spiciest_foods = [food for food in spicy_foods if food["heat_level"] > 5]
    return spiciest_foods

# function print_spicy_foods
# params: list of spicy_foods
# returns: outputs to the terminal each spicy food in the following format
#   print(): Buffalo Wing (American) | Heat Level: 🌶🌶🌶
def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        food_name = food["name"]
        food_cuisine = food["cuisine"]
        peppers = "🌶" * food["heat_level"]
        print(f"{food_name} ({food_cuisine}) | Heat Level: {peppers}")

# function get_spicy_food_by_cuisine
# params: list of spicy_foods and a string representing cuisine
# returns: single dictionary for the spicy food whose cuisine matches the cuisine being passed
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    spicy_cuisine = [food for food in spicy_foods if food["cuisine"] == cuisine]
    return spicy_cuisine[0]

# function print_spiciest_foods
# params: list of spicy_foods
# returns: outputs to the terminal ONLY the spicy foods with heat level > 5
def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)

# function get_average_heat_level
# params: list of spicy_foods
# returns: an interger representing the average heat level of all spicy foods
def get_average_heat_level(spicy_foods):
    length = len(spicy_foods)
    total = 0

    for food in spicy_foods:
        total += food["heat_level"]
    
    return math.floor(total/length)

# function create_spicy_foods
# params: list of spicy_foods and a new spicy_food
# returns: original list with the new spicy_food added
def create_spicy_food(spicy_foods, spicy_food):
    foods = spicy_foods + [spicy_food]
    return foods
