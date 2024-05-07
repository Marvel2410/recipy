from django.urls import path
from .views import home
from . import views



app_name = 'recipes'

urlpatterns = [
    path('', home, name='home'),
    path('recipe/<int:recipe_id>/', views.recipe_details, name='recipe_details'),
    path('recipes-list/', views.recipes_list, name='recipes_list'),
    path('search/', views.recipe_search, name='recipe_search'),

]