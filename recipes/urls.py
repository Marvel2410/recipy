from django.urls import path
from .views import home, recipe_details, recipes_list, add_recipe, edit_recipe, recipe_search

from . import views



app_name = 'recipes'

urlpatterns = [
    path('', home, name='home'),
    path('recipe/<int:recipe_id>/', views.recipe_details, name='recipe_details'),
    path('recipes-list/', views.recipes_list, name='recipes_list'),
    path('search/', views.recipe_search, name='recipe_search'),
    path('add-recipe/', add_recipe, name='add_recipe'),
    path('edit-recipe/<int:recipe_id>/', edit_recipe, name='edit_recipe'),
]