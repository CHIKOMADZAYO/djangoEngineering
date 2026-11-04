from django.urls import path
from . import views


# Add your app paths here

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('reports/', views.reports, name='reports'),
    path('analytics/', views.analytics, name='analytics'),
    path('login/', views.HomeView.as_view(), name='login_view'),
    path('register/', views.HomeView.as_view(), name='register_view'),
]


