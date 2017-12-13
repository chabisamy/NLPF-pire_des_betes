from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

from .models import Project, CounterPart, Participation


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


def project(request, project_id):
    project = Project.objects.get(pk=project_id)
    if request.POST.get('name', False) and request.POST.get('value', False) and request.user == project.author:
        CounterPart.objects.create(project=project, name=request.POST['name'], price=float(request.POST['value']))
        return redirect("index")
    else:
        return render(request, 'project.html', {'project': project})


def participate(request, counterpart_id):
    if request.user.is_authenticated:
        Participation.objects.create(author=request.user, counterpart_id=counterpart_id)
        return redirect("index")
    else:
        return redirect("index")