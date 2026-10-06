# KUNCI JAWABAN Fase 2 (A2). Jangan dibuka dulu sebelum coba sendiri.
# Ganti isi bagian "Fase 2" di main/views.py dengan kode ini.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, redirect, render

from main.forms import ProjectForm
from main.models import Project


def is_owner(user):
    return user.groups.filter(name='Owner').exists()


def is_editor(user):
    return user.groups.filter(name='Editor').exists()


@login_required(login_url='/login/')
def project_list(request):
    projects = Project.objects.select_related('owner').prefetch_related('starred_by')
    return render(request, 'project_list.html', {
        'projects': projects,
        'is_owner': is_owner(request.user),
        'is_editor': is_editor(request.user),
    })


@login_required(login_url='/login/')
def project_create(request):
    if not is_owner(request.user):
        return HttpResponseForbidden()
    form = ProjectForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        obj = form.save(commit=False)
        obj.owner = request.user
        obj.save()
        return redirect('main:project_list')
    return render(request, 'project_form.html', {'form': form, 'title': 'Buat project'})


@login_required(login_url='/login/')
def project_edit(request, pk):
    if not (is_owner(request.user) or is_editor(request.user)):
        return HttpResponseForbidden()
    project = get_object_or_404(Project, pk=pk)
    form = ProjectForm(request.POST or None, instance=project)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('main:project_list')
    return render(request, 'project_form.html', {'form': form, 'title': 'Edit project'})


@login_required(login_url='/login/')
def project_delete(request, pk):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])
    if not is_owner(request.user):
        return HttpResponseForbidden()
    get_object_or_404(Project, pk=pk).delete()
    return redirect('main:project_list')


@login_required(login_url='/login/')
def toggle_star(request, pk):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])
    project = get_object_or_404(Project, pk=pk)
    if request.user in project.starred_by.all():
        project.starred_by.remove(request.user)
    else:
        project.starred_by.add(request.user)
    return redirect('main:project_list')