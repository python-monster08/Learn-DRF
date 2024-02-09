from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
# Create your views here.

# ModelObject : Single Student Data (id=1)
def student_details(request,pk):
    stu = Student.objects.get(id=pk)
    serializer = StudentSerializer(stu)
    print(serializer.data)
    # json_data = JSONRenderer().render(serializer.data)
    # print(json_data)
    # return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(serializer.data)

# QuerySet : All Students Data 
def student_list(request):
    stu = Student.objects.all()
    print("Model Object",stu)
    serializer = StudentSerializer(stu,many=True)
    print("Serializer", serializer)
    print("Serialize Data",serializer.data)
    # json_data = JSONRenderer().render(serializer.data)
    # print("JSON Data",json_data)
    # return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(serializer.data,safe=False)
