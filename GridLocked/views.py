from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from GridLocked.models import Fighter, Equipment
from generator import *

@login_required(login_url='login')
def battles(request):
    """View function for battles page of site."""
    context={
        'currentPage' : "battles",
    }
    return render(request, 'battles.html', context=context)

@login_required(login_url='login')
def explore(request):
    """View function for explore page of site."""
    context={
        'currentPage' : "explore",
    }
    return render(request, 'explore.html', context=context)

@login_required(login_url='login')
def workshop(request):
    """View function for workshop page of site."""
    context={
        'currentPage' : "workshop",
    }
    return render(request, 'workshop.html', context=context)

def logout_view(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('explore')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def add_fighters_to_db(request):
    number_to_add = 1
    fighter_stat_array = make_random_fighter_stats(number_to_add)
    for fighter in fighter_stat_array:
        new_fighter = Fighter()
        new_fighter.name = "Test"
        new_fighter.energy_value = 0.0
        new_fighter.acid_value = 0.0
        new_fighter.metal_value = 0.0
        new_fighter.quantum_value = 0.0
        new_fighter.save()
    
    return redirect('workshop')

def delete_fighters(request):
    for fighter in Fighter.objects.all():
        fighter.delete()