from django.shortcuts import render, redirect

def battles(request):
    """View function for battles page of site."""
    context={
        'currentPage' : "battles",
    }
    return render(request, 'battles.html', context=context)

def explore(request):
    """View function for explore page of site."""
    context={
        'currentPage' : "explore",
    }
    return render(request, 'explore.html', context=context)

def workshop(request):
    """View function for workshop page of site."""
    context={
        'currentPage' : "workshop",
    }
    return render(request, 'workshop.html', context=context)