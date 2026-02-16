
def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed_type = seed_type.capitalize()
    if unit == "packets":
        print(seed_type, "seeds:", quantity, "packets available")
    elif unit == "grams":
        str_gram = "grams total"
        if quantity < 2:
            str_gram = "gram total"
        print(seed_type, "seeds:", quantity, str_gram)
    elif unit == "area":
        print(seed_type, "seeds: covers", quantity, "square meters")
    else:
        print("Unknow unit type")

# ft_seed_inventory("parrote", 2, "area")
