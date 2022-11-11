from django.shortcuts import render, redirect

from Recipies.web.forms import CreateRecipeForm, EditRecipeForm, DeleteRecipeForm
from Recipies.web.models import Recipe


# Create your views here.
def get_receipt():
    receipts = Recipe.objects.all()
    if receipts:
        return receipts


def home_page(request):
    receipts = get_receipt()
    context = {
        'receipts': receipts,
        'create': True,
    }
    return render(request, template_name='index.html', context=context)


def create_recipe(request):
    if request.method == 'POST':
        form = CreateRecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = CreateRecipeForm()
    context = {
        'form': form,
    }
    return render(request, template_name='create.html', context=context)


def edit_recipe(request, pk):
    receipt = Recipe.objects.filter(pk=pk).get()
    if request.method == 'POST':
        form = EditRecipeForm(request.POST, instance=receipt)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = EditRecipeForm(instance=receipt)
    context = {
        'form': form,
    }
    return render(request, template_name='edit.html', context=context)


def delete_recipe(request, pk):
    receipt = Recipe.objects.filter(pk=pk).get()
    if request.method == 'POST':
        form = DeleteRecipeForm(request.POST, instance=receipt)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = DeleteRecipeForm(instance=receipt)
    context = {
        'form': form
    }
    return render(request, template_name='delete.html', context=context)


def recipe_details(request, pk):
    receipt = Recipe.objects.filter(pk=pk).get()
    ingredients = [x for x in receipt.ingredients.split(', ')]
    context = {
        'receipt': receipt,
        'ingredients': ingredients
    }
    return render(request, template_name='details.html', context=context)
