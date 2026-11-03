from django.urls import path
from . import views


# Add your app paths here

urlpatterns = [
    path('', views.home, name='home')
]


