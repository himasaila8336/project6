from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def dhoni(request):
    return HttpResponse('msd is the best finisher in the world')