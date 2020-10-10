from django import forms

from .models import UnitType


class RecipeForm(forms.ModelForm):
    name = forms.CharField(label='Name', max_length=100)
    description = forms.CharField(label='Your recipe', max_length=10000)


class Recipe2IngredientForm(forms.ModelForm):
    ingredient = forms.ChoiceField(label='Ingredient')
    quantity = forms.FloatField(label='quantity')
    unit_type = forms.ChoiceField(choices=UnitType)
