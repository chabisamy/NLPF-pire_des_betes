from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import Context, loader

def home(request):
    return render_to_response('home/templates/home.html')
