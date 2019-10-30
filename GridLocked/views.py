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
    number_to_add = 10
    fighter_stat_list = make_random_fighter_stats(number_to_add)
    for fighter in fighter_stat_list:
        new_fighter = Fighter()
        freename = "FL_"
        for digit in fighter:
            freename += str(int(digit))
        new_fighter.name = freename
        new_fighter.energy_value = STAT_MULTIPLIER_SET[fighter[0]-1]
        new_fighter.acid_value = STAT_MULTIPLIER_SET[fighter[1]-1]
        new_fighter.metal_value = STAT_MULTIPLIER_SET[fighter[2]-1]
        new_fighter.quantum_value = STAT_MULTIPLIER_SET[fighter[3]-1]
        new_fighter.save()
    return redirect('workshop')

def delete_fighters(request):
    for fighter in Fighter.objects.all():
        fighter.delete()
    return redirect('workshop')

def add_weapons_to_db(request):
    number_to_add = 10
    weapon_name_list = weapon_name_list_generator(number_to_add)
    for weapon_name in weapon_name_list:
        new_weapon = Equipment()
        new_weapon_words = weapon_name.split()
        new_weapon.name = weapon_name
        new_weapon.force = 1
        new_weapon.attribute = new_weapon_words[0][0].upper
        if new_weapon_words[1] == "Blaster":
            new_weapon.weapon_range = 2
            new_weapon.min_range_offest = 2
            new_weapon.area_of_effect = 1
        elif new_weapon_words[1] == "Cannon":
            new_weapon.weapon_range = 6
            new_weapon.min_range_offest = 0
            new_weapon.area_of_effect = 0
        elif new_weapon_words[1] == "Blade":
            new_weapon.weapon_range = 1
            new_weapon.min_range_offest = 0
            new_weapon.area_of_effect = 0
        elif new_weapon_words[1] == "Bomb":
            new_weapon.weapon_range = 10
            new_weapon.min_range_offest = 3
            new_weapon.area_of_effect = 2
        new_weapon.save()
    return redirect('workshop')

def delete_weapons(request):
    for weapon in Equipment.objects.all():
        weapon.delete()
    return redirect('workshop')