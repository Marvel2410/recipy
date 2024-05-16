from django.test import TestCase, Client
from django.urls import reverse
from .models import Recipe
from .forms import RecipeSearchForm, RecipeForm
from django.contrib.auth.models import User

def create_recipe(name='Test Recipe', description='Test Description', cooking_time=30, ingredients='Ingredient1,Ingredient2,Ingredient3', difficulty_level='easy', user=None):
    if user is None:
        user = User.objects.create_user(username='uniqueuser', password='12345')
    return Recipe.objects.create(
        user=user,
        name=name,
        description=description,
        cooking_time=cooking_time,
        ingredients=ingredients,
        difficulty_level=difficulty_level
    )

class RecipeModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='12345')
        cls.recipe = create_recipe(user=cls.user)

    def test_recipe_name(self):
        self.assertEqual(self.recipe.name, 'Test Recipe')

    def test_cooking_time(self):
        self.assertEqual(self.recipe.cooking_time, 30)

    def test_difficulty_level(self):
        self.recipe.difficulty_level = 'hard'
        self.recipe.save()
        self.assertEqual(self.recipe.difficulty_level, 'hard')

    def test_name_max_length(self):
        max_length = Recipe._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)

class RecipeViewsTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser_views', password='12345')
        cls.recipe = create_recipe(user=cls.user)

    def setUp(self):
        self.client = Client()
        self.client.login(username='testuser_views', password='12345')

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

    def test_add_recipe_view(self):
        # Ensure this URL and modal is being tested correctly
        response = self.client.get(reverse('recipes:recipes_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Add Recipe')

        form_data = {
            'name': 'New Recipe',
            'description': 'New Description',
            'cooking_time': 20,
            'ingredients': 'Ingredient1, Ingredient2',
            'difficulty_level': 'easy',
            'category': 'lunch',
        }
        response = self.client.post(reverse('recipes:add_recipe'), data=form_data)
        self.assertEqual(response.status_code, 302)  # Should redirect after successful post

class RecipeFormsTest(TestCase):

    def test_recipe_search_form(self):
        form_data = {
            'name': 'Test',
            'ingredient': 'Ingredient1',
            'difficulty_level': 'easy',
            'category': 'lunch',
            'show_all': True,
            'chart_type': '#1',
        }
        form = RecipeSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_recipe_form(self):
        form_data = {
            'name': 'Test Recipe',
            'description': 'Test Description',
            'cooking_time': 30,
            'ingredients': 'Ingredient1, Ingredient2',
            'difficulty_level': 'easy',
            'category': 'lunch',
        }
        form = RecipeForm(data=form_data)
        self.assertTrue(form.is_valid())

class RecipeDetailViewTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser_detail', password='12345')
        cls.recipe = create_recipe(user=cls.user)

    def setUp(self):
        self.client = Client()
        self.client.login(username='testuser_detail', password='12345')

    def test_recipe_detail_view(self):
        response = self.client.get(reverse('recipes:recipe_details', args=[self.recipe.id]))
        self.assertEqual(response.status_code, 200)

    def test_recipe_detail_view_invalid(self):
        response = self.client.get(reverse('recipes:recipe_details', args=[9999]))
        self.assertEqual(response.status_code, 404)

class RecipeListViewTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser_list', password='12345')

    def setUp(self):
        self.client = Client()
        self.client.login(username='testuser_list', password='12345')

    def test_recipe_list_view(self):
        response = self.client.get(reverse('recipes:recipes_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes/recipes_list.html')
