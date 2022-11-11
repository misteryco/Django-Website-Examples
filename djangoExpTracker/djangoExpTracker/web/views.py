from django.shortcuts import render, redirect

from djangoExpTracker.web.forms import CreateProfileFrom, EditProfileFrom, DeleteProfileFrom, CreateExpenseFrom, \
    EditExpenseFrom, DeleteExpenseFrom
from djangoExpTracker.web.models import Profile, Expense


def get_profile():
    profile = Profile.objects.first()
    if profile:
        return profile


# Create your views here.
def home_page(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')

    total_expenses = Expense.objects.all()
    budget_left = profile.budget - sum(exp.price for exp in total_expenses)

    context = {
        'profile': profile,
        'total_expenses': total_expenses,
        'budget_left': budget_left,
    }

    return render(request, template_name='home-with-profile.html', context=context)


def create_expense(request):
    if request.method == 'POST':
        form = CreateExpenseFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = CreateExpenseFrom()

    context = {
        'form': form
    }
    return render(request, 'expense-create.html', context=context)


def edit_expense(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditExpenseFrom(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = EditExpenseFrom(instance=expense)

    context = {
        'form': form
    }
    return render(request, 'expense-edit.html', context=context)


def delete_expense(request, pk):
    expense = Expense.objects.get(pk=pk)

    if request.method == 'POST':
        form = DeleteExpenseFrom(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = DeleteExpenseFrom(instance=expense)

    context = {
        'form': form,
        'expense': expense,
        'pk': pk,
    }
    return render(request, 'expense-delete.html', context=context)


def profile(request):
    profile = get_profile()
    total_expenses = Expense.objects.all()
    budget_left = profile.budget - sum(exp.price for exp in total_expenses)
    context = {
        'profile': profile,
        'expenses_count': len(total_expenses),
        'budget_left': budget_left
    }
    return render(request, 'profile.html', context=context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileFrom(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = CreateProfileFrom()
    context = {
        'form': form,
        'no_profile': True
    }
    return render(request, 'home-no-profile.html', context=context)


def edit_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = EditProfileFrom(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            # return render(request, 'home-with-profile.html', )
    else:
        form = EditProfileFrom(instance=profile)

    context = {
        'form': form
    }
    return render(request, 'profile-edit.html', context=context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteProfileFrom(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = DeleteProfileFrom(instance=profile)

    context = {
        'form': form
    }
    return render(request, 'profile-delete.html', context=context)
