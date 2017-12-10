from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django import forms
from .forms import ProjectForm
from .models import Project


# Create your views here.
def index(request):
    projects_list = Project.objects.order_by('-published_date')
    return render(request, 'index.html', {'projects_list': projects_list})


def new_project(request):
    if request.user.is_authenticated:
        if request.POST.get('name', False) and request.POST.get('description', False):
            Project.objects.create(name=request.POST['name'], description=request.POST['description'], author=request.user)
            return redirect("index")
        else:
            return render(request, 'new_project.html')
    else:
        return redirect("login")

def project_details(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'project.html', {'project': project})

def add_counterpart(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.POST.get('name', False) and request.POST.get('description', False):
            Project.objects.create(project=request.project, name=request.POST['name'], description=request.POST['price'])
            return redirect("project")
    else:
        return render(request, 'counterpart.html')