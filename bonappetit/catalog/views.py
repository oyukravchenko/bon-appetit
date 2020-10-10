from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.forms import formset_factory, inlineformset_factory
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader

from catalog.models import Recipes, UnitType, Ingredients, Recipe2Ingredient
from django.urls import reverse
from django.utils import timezone

from catalog.forms import RecipeForm
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'catalog/index.html'
    context_object_name = 'latest_recipes_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Recipes.objects.order_by('-create_date')[:5]


class UserProfileView(generic.DetailView):
    pass


class RecipeDetailsView(generic.DetailView):
    model = Recipes
    template_name = 'catalog/recipe_details.html'


IngredientsFormSet = inlineformset_factory(Recipes, Recipe2Ingredient, fields=('ingredient', 'quantity', 'unit'))


class RecipeWithIngredientsView(LoginRequiredMixin, generic.CreateView):
    model = Recipes
    fields = ['name', 'description']
    template_name = 'catalog/new_recipe.html'

    def get_context_data(self, **kwargs):
        # we need to overwrite get_context_data
        # to make sure that our formset is rendered
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data["ingredients"] = IngredientsFormSet(self.request.POST)
        else:
            data["ingredients"] = IngredientsFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        ingredients = context["ingredients"]
        form.instance.author = self.request.user
        self.object = form.save()
        if ingredients.is_valid():
            ingredients.instance = self.object
            ingredients.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("catalog:recipe_details", kwargs={'pk': self.object.id})


def index(request):
    latest_recipes_list = Recipes.objects.order_by('-create_date')[:5]
    ingredients = Ingredients.objects.all()

    print("Got {} recipes".format(len(latest_recipes_list)))

    template = loader.get_template('catalog/index.html')
    context = {
        'latest_recipes_list': latest_recipes_list,
        'unit_type_set': UnitType.labels,
        'ingredients': ingredients,
        'form': RecipeForm()
    }
    return HttpResponse(template.render(context, request))


def user_profile(request, user_id):
    return HttpResponse("You can manage your profile here. UserId = %s" % user_id)


def save_recipe(request):
    print(request.POST)
    new_recipe = Recipes(name=request.POST['name'], description=request.POST['description'], create_date=timezone.now())
    user = request.user()
    new_recipe.author = user
    new_recipe.save()

    return HttpResponseRedirect(reverse('catalog:recipe_details', args=(new_recipe.id,)))


def recipes(request, recipe_id):
    recipe = get_object_or_404(Recipes, pk=recipe_id)
    return render(request, 'catalog/recipe_details.html', {'object': recipe})


@login_required(login_url='/accounts/login/')
def my_recipes(request, user_id):
    user = User.objects.get(pk=user_id)
    print("User=", user)
    recipes_by_user = Recipes.objects.all().filter(author=user)
    return render(request, 'catalog/my_recipes.html', {'recipes_list': recipes_by_user})

