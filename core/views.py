from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    template_name='core/home.html'
    return render(request, template_name)

def search(request):
    template_name='core/search.html'
    return render(request, template_name)