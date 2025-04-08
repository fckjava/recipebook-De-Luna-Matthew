from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Recipe, Ingredient, RecipeIngredient, Profile, RecipeImage

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False 

class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline,]

class RecipeImageInline(admin.StackedInline):
    model = RecipeImage
    can_delete = False

class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeImageInline,]

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)
admin.site.register(RecipeIngredient)
admin.site.register(Profile)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
