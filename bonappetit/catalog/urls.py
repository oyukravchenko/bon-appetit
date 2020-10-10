
from django.urls import path

from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('profile/<int:user_id>/', views.UserProfileView.as_view(), name='my_profile'),
    path('recipes/<int:pk>/', views.RecipeDetailsView.as_view(), name='recipe_details'),
    path('recipes/author/<int:user_id>/', views.my_recipes, name='my_recipes'),
    path('recipes/save', views.save_recipe, name='create_recipe'),
    path('recipes/create', views.RecipeWithIngredientsView.as_view(), name='new_recipe'),
]