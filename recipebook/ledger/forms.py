from django import forms
from .models import RecipeImage, Recipe

class RecipeImageForm(forms.ModelForm):
    class Meta:
        model = RecipeImage
        fields = '__all__'

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'