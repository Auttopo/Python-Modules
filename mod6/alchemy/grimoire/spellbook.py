
def record_spell(spell_name: str, ingredients: str) -> str:
    from alchemy.grimoire import validator
    result = validator.validate_ingredients(ingredients).split(" ")
    if result[len(result) - 1] == "VALID":
        return f"Spell recorded: {spell_name} {result}"
    return f"Spell rejected: {spell_name} {result}"
