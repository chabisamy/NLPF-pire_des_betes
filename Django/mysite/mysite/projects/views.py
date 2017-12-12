from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django import forms
from .forms import ProjectForm
from .models import Project
from .models import CounterPart


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

def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.user.is_authenticated and request.user.username == project.author.username:
        project = get_object_or_404(Project, pk=pk)
        if request.method == "POST":
            form = ProjectForm(request.POST, instance=project)
            if form.is_valid():
                project = form.save(commit=False)
                project.author = request.user
                project.name = request.name
                project.description = request.description
                project.save()
                return redirect('project', pk=project.pk)
        else:
            form = ProjectForm(instance=project)
        return render(request, 'project_edit.html', {'form': form})


def project_details(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'project.html', {'project': project})

def add_counterpart(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.POST.get('name', False) and request.POST.get('price', False):
        project = get_object_or_404(Project, pk=pk)
        CounterPart.objects.create(project=project, name=request.POST['name'], price=request.POST['price'])
        return render(request, 'project.html', {'project': project})
    else:
            return render(request, 'counterpart.html')
    