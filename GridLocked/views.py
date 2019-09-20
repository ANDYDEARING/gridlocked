from django.shortcuts import render, redirect

def battles(request):
    """View function for battles page of site."""
    context={

    }
    return render(request, 'battles.html', context=context)