from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Ingredients, Recipe2Ingredient, UnitType, Recipes


class IngredientsAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        ('Nutritions', {'fields': ['proteins', 'fats', 'carbonhydrates', 'calories']}),
    ]


class IngredientsInline(admin.TabularInline):
    model = Ingredients
    extra = 3


class Recipe2IngredientsAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['recipe']}),
        ('Ingredient list', {'fields': ['ingredient', 'quantity', 'unit']}),
    ]


class Recipe2IngredientsInline(admin.TabularInline):
    model = Recipe2Ingredient
    extra = 3


class RecipesAdmin(admin.ModelAdmin):
    fields = ['name', 'description']
    inlines = [Recipe2IngredientsInline]

    def save_model(self, request, obj, form, change):
        if not obj.author_id:
            obj.author = request.user
        # obj.last_modified_by = request.user
        obj.save()

admin.site.register(Ingredients, IngredientsAdmin)
admin.site.register(Recipe2Ingredient, Recipe2IngredientsAdmin)
admin.site.register(Recipes, RecipesAdmin)


