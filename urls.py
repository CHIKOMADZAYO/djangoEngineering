from django.urls import path
from . import views



urlpatterns = [
    path('persons/', views.PersonListView.as_view(), name='person_list'),
    path('courses/', views.CourseListView.as_view() , name='course_list'),
]