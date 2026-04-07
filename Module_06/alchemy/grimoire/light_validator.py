def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients
    allowed = light_spell_allowed_ingredients()
    if any(ingredient in ingredients.lower() for ingredient in allowed):
        return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"
