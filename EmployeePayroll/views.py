"""
To render HTML webpages
"""
from typing import ContextManager
from django.shortcuts import render
from django import template
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate




# **************************************************************************
@login_required
def home_view(request):

    return render(request,'home-view.html', {})