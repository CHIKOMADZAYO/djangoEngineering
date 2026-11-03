from django.views import View
from django.http import JsonResponse

from models import Person




class PersonListView(View):
    def get(self, request):
        persons = Person.objects.all()
        data = [{"id": person.id, "name": person.name, "age": person.age, "email": person.email, "course": person.course} for person in persons]
        return JsonResponse(data, safe=False)