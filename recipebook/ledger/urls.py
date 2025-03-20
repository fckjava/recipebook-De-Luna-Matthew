from django.urls import path
from .views import recipe_list, recipe_detail

urlpatterns = [
    path('recipes/list/', recipe_list, name ='recipes'),
    path('recipe/<int:recipe_id>/', recipe_detail, name='recipe_detail'),
]

app_name = "ledger"

