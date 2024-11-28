from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def prabhas(request):
    return HttpResponse('prabhas is the tollywood hero')
def alluarjun(request):
    return HttpResponse('alluarjun is the hero of the tollywood')


