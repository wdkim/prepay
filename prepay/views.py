from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404

def index(request):
    return render(request, 'prepay/home.html')