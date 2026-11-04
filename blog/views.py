from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def reports(request):
    return render(request, 'reports.html')


def analytics(request):
    return render(request, 'analytics.html')
