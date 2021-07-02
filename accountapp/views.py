from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def nd_project(request):
    return render(request, 'base.html')