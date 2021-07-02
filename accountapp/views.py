from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def write_correct(request):
    return HttpResponse("얘들아 맞춤법 지키자!")