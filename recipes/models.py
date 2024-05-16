from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

def get_default_user():
    User = get_user_model()
    user = User.objects.first()
    if user is None:
        user = User.objects.create(username='defaultuser', password='defaultpassword')
    return user.id

class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=get_default_user)
    name = models.CharField(max_length=100)
    description = models.TextField()
    cooking_time = models.IntegerField()
    ingredients = models.TextField()
    difficulty_level_choices = (
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    )
    difficulty_level = models.CharField(max_length=10, choices=difficulty_level_choices)
    pic = models.ImageField(upload_to='recipes', default='no_image.jpg')
    category_choices = (
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('snack', 'Snack'),
        ('dessert', 'Dessert'),
    )
    category = models.CharField(max_length=10, choices=category_choices, default='lunch')

    def __str__(self):
        return self.name