"""
Views for the listings app.
"""
from django.shortcuts import render

from django.contrib.auth.decorators import login_required


@login_required
def add_listing(request):
    """
    A view for users to create a listing on the site.
    """
    template = 'listings/add_listing.html'
    return render(request, template)
