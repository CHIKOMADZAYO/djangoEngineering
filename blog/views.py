from django.shortcuts import render
from django.views import View

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


class HomeView(View):
    def get(self, request):
        return render(request, 'login.html')
    

    


clas

