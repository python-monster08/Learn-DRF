# GenericApiView & Model Mixin

from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin

# Create your ModelMixin Class Here...

class StudentList(GenericAPIView, ListModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def get(self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs)
