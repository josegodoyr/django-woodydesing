from django.shortcuts import redirect, render

from .models import Project
from .forms import ProjectForm
# Create your views here.

def inicio(request):
    projects = Project.objects.all().order_by('-fecha_inicio')[:5]

    return render(request, 'paginas/inicio.html', {'projects': projects})

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def test(request):
    return render(request, 'proyectos/index.html')
    
def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects/index.html', {'projects': projects})

def add_projects(request):
    form = ProjectForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('projects')
    return render(request, 'projects/add_projects.html', {'form': form})

def edit_projects(request, id):
    project = Project.objects.get(id=id)
    form = ProjectForm(request.POST or None, instance = project)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('projects')
    return render(request, 'projects/edit_projects.html', {'form':form})

def delete_projects(request):
    return render(request, 'projects/delete_projects.html')