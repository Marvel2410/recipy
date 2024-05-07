from django.db import models
from .storage import OverwriteStorage

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    cooking_time = models.IntegerField()
    ingredients = models.TextField()

    DIFFICULTY_LEVELS = (
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    )
    difficulty_level = models.CharField(max_length=10, choices=DIFFICULTY_LEVELS)

    pic = models.ImageField(upload_to='recipes/', storage=OverwriteStorage())

    CATEGORY_CHOICES = (
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('snack', 'Snack'),
        ('dessert', 'Dessert'),
    )
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='lunch')

    def __str__(self):
        return self.name
