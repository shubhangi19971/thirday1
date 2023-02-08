from rest_framework import viewsets
from.serializers import Person, PersonSerializer



class PersonViewSet(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()
