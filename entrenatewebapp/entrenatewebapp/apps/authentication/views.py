from typing import List, Dict, Any
from django.shortcuts import render, redirect

# Create your views here.
def sign_up(request: Any):
    context = {}
    return render(request=request, template_name='authentication/signup.html', context=context)

def login(request: Any):
    context = {}
    return render(request=request, template_name='authentication/login.html', context=context)

