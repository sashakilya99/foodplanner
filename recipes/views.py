from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe
from .forms import RecipeForm


def home(request):
    recipes = Recipe.objects.all().order_by('-created_at')
    return render(request, 'recipes/home.html', {'recipes': recipes})


def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})


def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RecipeForm()

    return render(request, 'recipes/recipe_form.html', {'form': form})


def recipe_update(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)

        if form.is_valid():
            form.save()
            return redirect('recipe_detail', recipe_id=recipe.id)
    else:
        form = RecipeForm(instance=recipe)

    return render(
        request,
        'recipes/recipe_form.html',
        {'form': form, 'recipe': recipe}
    )


def recipe_delete(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if request.method == 'POST':
        recipe.delete()
        return redirect('home')

    return render(
        request,
        'recipes/recipe_confirm_delete.html',
        {'recipe': recipe}
    )