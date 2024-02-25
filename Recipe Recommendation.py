class RecipeRecommendation:
    def __init__(self):
        self.recipes = {"Pasta": ["tomato", "pasta", "garlic"], "Salad": ["lettuce", "tomato", "cucumber"]}

    def recommend_recipe(self, ingredients):
        for recipe, recipe_ingredients in self.recipes.items():
            if all(ingredient in recipe_ingredients for ingredient in ingredients):
                return recipe
        return "No matching recipe found."

# Example usage:
recommendation = RecipeRecommendation()
ingredients = ["lettuce", "tomato", "cheese"]
recipe = recommendation.recommend_recipe(ingredients)
print(f"Recommended recipe: {recipe}")
