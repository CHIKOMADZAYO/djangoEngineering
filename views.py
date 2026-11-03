from django.views import View
from django.http import JsonResponse

from models import Person




class PersonListView(View):
    def get(self, request):
        persons = Person.objects.all()
        data = [{"id": person.id, "name": person.name, "age": person.age, "email": person.email, "course": person.course} for person in persons]
        return JsonResponse(data, safe=False)


    def post(self, request):
        # Handle POST request to create a new person
        pass

    def put(self, request, person_id):
        # Handle PUT request to update an existing person
        pass

    def delete(self, request, person_id):

        pass
    
