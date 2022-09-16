from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Project
from .forms import ProjectForm


def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'project/projects.html', context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    return render(request, 'project/single-project.html', {'project': projectObj, 'tags': tags})


@login_required(login_url='login-user')
def create_project(request):
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, 'project/project-form.html', context)


@login_required(login_url='login-user')
def update_project(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form': form}
    return render(request, 'project/project-form.html', context)


@login_required(login_url='login-user')
def delete_project(request, pk):
    project = Project.objects.get(id=pk)
    context = {'object': project}
    if request.method == "POST":
        project.delete()
        return redirect('projects')
    return render(request, 'project/delete-project.html', context)