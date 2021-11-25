"""
To render HTML webpages
"""
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.template.loader import render_to_string

def home_view(request):

    HTML_STRING = render_to_string("home-view.html")
    return HttpResponse(HTML_STRING)