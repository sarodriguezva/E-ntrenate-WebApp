from typing import List, Dict, Any
from django.shortcuts import render, redirect

from django.contrib.auth import logout

def home(request: Any):
    """
    Vista de Home
    """
    context = {'base_template': "basetemplate.html"}

    if request.user.is_authenticated:
        context['base_template'] = "basetemplate_loggedin.html"

    return render(request=request, template_name="home/home.html", context=context)
