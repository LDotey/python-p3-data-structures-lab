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

def get_names(spicy_foods):
    return [food.get("name") for food in spicy_foods]
    pass

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food.get("heat_level") > 5]
    pass

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"]
        heat_level_str = "🌶" * heat_level
        print(f"{name} ({cuisine}) | Heat Level: {heat_level_str}")
    pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food.get("cuisine") == cuisine:
            return food
    pass

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        heat_level = food.get("heat_level")
        if heat_level > 5:
            name = food.get("name")
            cuisine = food.get("cuisine")
            heat_level_str = "🌶" * heat_level
            print(f"{name} ({cuisine}) | Heat Level: {heat_level_str}")

    pass

def get_average_heat_level(spicy_foods):
    all_heat = sum(food.get("heat_level") for food in spicy_foods)
    avg_heat = all_heat / len(spicy_foods)
    return avg_heat
    pass

def create_spicy_food(spicy_foods, spicy_food):
    return spicy_foods + [spicy_food]
    pass
