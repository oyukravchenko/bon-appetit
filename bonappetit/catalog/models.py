from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.
# class Users(models.Model):
#     login = models.CharField(max_length=30, primary_key=True)
#     name = models.CharField(max_length=30)
#     last_login = models.DateTimeField()
#     create_date = models.DateTimeField()
#
#     def __str__(self):
#         return self.login


class Recipes(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    create_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.name


class Ingredients(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    proteins = models.FloatField(default=0)
    fats = models.FloatField(default=0)
    carbonhydrates = models.FloatField(default=0)
    calories = models.FloatField(default=0)

    def __str__(self):
        return self.name


class UnitType(models.TextChoices):
    KG = 'kg'
    G = 'g'
    L = 'l'
    ML = 'ml'
    PIECES = 'pcs'
    SPOON = 'sp'
    TEA_SPOON = 'tsp'
    GLASS = 'gls'
    CLOVE = 'clove'


class Recipe2Ingredient(models.Model):
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredients, on_delete=models.CASCADE)
    quantity = models.FloatField()
    unit = models.CharField(max_length=10, choices=UnitType.choices)

    def __str__(self):
        return str(self.recipe) + ": " + str(self.ingredient) + " - " + str(self.quantity) + " " + str(self.unit)
