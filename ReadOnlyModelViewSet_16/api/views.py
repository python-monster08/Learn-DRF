from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets

# Create your views here

class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer