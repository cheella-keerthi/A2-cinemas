from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def tom(request):
    return HttpResponse('tom is the hollywood hero')
def vin(request):
    return HttpResponse('vin is the hollywood hero')