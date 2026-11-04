from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

# def home(request):
#     return render(request, 'home.html')


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Welcome to the Home Page!'
        return context
    


