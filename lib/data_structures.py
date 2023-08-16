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
    return [f["name"] for f in spicy_foods]


def get_spiciest_foods(spicy_foods):
    return [f for f in spicy_foods if f["heat_level"] > 5]


def print_spicy_foods(spicy_foods):
    return [print(f'{f["name"]} ({f["cuisine"]}) | Heat Level: {"🌶" * f["heat_level"]}') for f in spicy_foods]


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    return [f for f in spicy_foods if f["cuisine"] == cuisine][0]


def print_spiciest_foods(spicy_foods):
    foods = get_spiciest_foods(spicy_foods)
    return print_spicy_foods(foods)


def get_average_heat_level(spicy_foods):
    return sum([f["heat_level"] for f in spicy_foods]) / len(spicy_foods)


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
