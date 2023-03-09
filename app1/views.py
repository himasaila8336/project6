from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def dhoni(request):
    return HttpResponse('<h1>msd is the best finisher in the world</h1>')
def hima(request):
    return HttpResponse('<h1> hima is good girl<h1>')    