

from django.shortcuts import render
# Create your views here.

from utils.recipes.factory import make_recipe


def home(request):
        
    return render(request, "recipes/pages/home.html", context={
        'recipes': [make_recipe() for _ in range(10)]
    })


def recipes(request, id):
        
    return render(request, "recipes/pages/recipe-view.html", context={
        'recipe': make_recipe()
    })


