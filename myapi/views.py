from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import StudentSerializer
from .models import Student
from rest_framework import viewsets


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def list(self, request, *args, **kwargs):
        serializer = StudentSerializer(Student.objects.all(), many=True)
        return Response(serializer.data)

