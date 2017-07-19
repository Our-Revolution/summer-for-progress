"""Views for the summerforprogress app"""

from django.shortcuts import render


def home(request):
    """ Default view for the root """
    return render(request, 'base/home.html')

def platform(request):
    """ View for the People's Platform """
    return render(request, 'base/platform.html')

def petition(request):
    """ View for the petition """
    return render(request, 'base/petition.html')

def get_involved(request):
    """ View for the get involved page """
    return render(request, 'base/get-involved.html')
