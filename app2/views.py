from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def virat(request):
    return HttpResponse('<h1> virat best batsman in the world</h1>')
def sasi(request):
    return HttpResponse('<h1><marquee> sasi is my brother</marquee></h1>')    
