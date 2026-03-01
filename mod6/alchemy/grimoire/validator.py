
def validate_ingredients(ingredients: str) -> str:
    items = ingredients.split(" ")
    for item in items:
        if not simple_validation(item):
            return f"{ingredients} - INVALID"
    return f"{ingredients} - VALID"


def simple_validation(data: str) -> bool:
    if data == "fire":
        return True
    elif data == "water":
        return True
    elif data == "earth":
        return True
    elif data == "air":
        return True
    return False
