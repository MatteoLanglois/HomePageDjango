from django.http import request
from django.shortcuts import render

from . import models

def index(request):
    projects = models.Project.objects.all().filter(visible=True)
    return render(request, 'home/index.html', context= {
        'projects': projects,
    })
