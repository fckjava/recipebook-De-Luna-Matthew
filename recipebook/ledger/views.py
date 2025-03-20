from django.shortcuts import render
from .models import Recipe

def recipe_list(request):
    recipes = Recipe.objects.all()
    ctx = {'recipes': recipes}
    return render(request, 'ledger/recipe_list.html', ctx)

def recipe_detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    ctx = {'recipe': recipe}
    return render(request, 'ledger/recipe_detail.html', ctx)

