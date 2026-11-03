from django.urls import path
from . import views



urlpatterns = [
    path('persons/', views.person_list, name='person_list'),
    path('courses/', views.course_list, name='course_list'),
]