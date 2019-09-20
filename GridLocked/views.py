from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

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