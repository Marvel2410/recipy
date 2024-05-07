from django.test import TestCase, Client
from django.urls import reverse
from .models import Recipe
from .forms import RecipeSearchForm
from .views import RecipeListView, RecipeDetailView, recipe_search
from django.contrib.auth.models import User

def create_recipe(name='Test Recipe', description='Test Description', cooking_time=30, ingredients='Ingredient1,Ingredient2,Ingredient3', difficulty_level='easy'):
    return Recipe.objects.create(
        name=name,
        description=description,
        cooking_time=cooking_time,
        ingredients=ingredients,
        difficulty_level=difficulty_level
    )

class RecipeModelTest(TestCase):
    
    def test_recipe_name(self):
        recipe = create_recipe()
        self.assertEqual(recipe.name, 'Test Recipe')

    def test_cooking_time(self):
        recipe = create_recipe()
        self.assertEqual(recipe.cooking_time, 30)

    def test_difficulty_level(self):
        recipe = create_recipe(difficulty_level='hard')
        self.assertEqual(recipe.difficulty_level, 'hard')

    def test_name_max_length(self):
        max_length = Recipe._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)

class RecipeViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.recipe = create_recipe()

    def test_home_view(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes/recipes_home.html')

    def test_recipe_details_view(self):
        response = self.client.get(reverse('recipes:recipe_details', args=[self.recipe.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes/recipe_details.html')

    def test_recipes_list_view(self):
        response = self.client.get(reverse('recipes:recipes_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes/recipes_list.html')

    def test_recipe_search_view(self):
        response = self.client.get(reverse('recipes:recipe_search'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes/recipe_search.html')


class RecipeDetailViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.recipe = create_recipe()
        self.client.login(username='testuser', password='12345')

    def test_recipe_detail_view(self):
        response = self.client.get(reverse('recipes:recipe_details', args=[self.recipe.id]))
        self.assertEqual(response.status_code, 200)

    def test_recipe_detail_view_invalid(self):
        with self.assertRaises(Recipe.DoesNotExist):
            response = self.client.get(reverse('recipes:recipe_details', args=[self.recipe.id + 1]))

class RecipeListViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_recipe_list_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('recipes:recipes_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes/recipes_list.html')
 