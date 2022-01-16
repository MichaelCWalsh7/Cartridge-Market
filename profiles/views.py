"""
Views for the profiles app.
"""
from django.shortcuts import render


def profile(request):
    """
    Displays the user's profile.
    """
    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)
