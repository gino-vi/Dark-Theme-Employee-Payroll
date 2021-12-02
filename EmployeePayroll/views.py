"""
To render HTML webpages
"""
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect

def home_view(request):

    return render(request, "home-view.html", {})