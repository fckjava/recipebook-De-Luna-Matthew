from django.shortcuts import render
from .models import Recipe, RecipeIngredient, RecipeImage
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import RecipeImageForm, RecipeForm

@login_required
def recipe_list(request):
    recipes = Recipe.objects.all()
    ctx = {'recipes': recipes}
    return render(request, 'ledger/recipe_list.html', ctx)

@login_required
def recipe_detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    ctx = {'recipe': recipe}
    return render(request, 'ledger/recipe_detail.html', ctx)

@login_required
def add_image(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    form = RecipeImageForm()
    if request.method == 'POST':
        form = RecipeImageForm(request.POST, request.FILES)
        if form.is_valid():
            i = RecipeImage()
            i.description = form.cleaned_data.get('description')
            i.image = form.cleaned_data.get('image')
            i.recipe = recipe
            i.save()
            return redirect('ledger:recipe_detail', recipe_id=recipe.pk)

    ctx = { 'form': form, 'recipe': recipe}
    return render(request, 'ledger/add_image.html', ctx)

@login_required
def add_recipe(request):
    form = RecipeForm()
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ledger:recipe_list')
    
    ctx = { 'form': form}
    return render(request, 'ledger/add_recipe.html', ctx)