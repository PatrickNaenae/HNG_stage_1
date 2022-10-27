from rest_framework import viewsets

from .serializers import StudentSerializer
from .models import Student


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('name')
    serializer_class = StudentSerializer
