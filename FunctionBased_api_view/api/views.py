from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

# GET API
# @api_view()
# def hello_world(request):
#     return Response({'msg':'Hello World'})

# GET API with GET Parameter
# @api_view(['GET'])
# def hello_world(request):
#     return Response({'msg':'Hello World'})

# # POST API with POST Parameter
# @api_view(['POST'])
# def hello_world(request):
#     if request.method == "POST":
#         print(request.data)
#         return Response({'msg':'Called Post method'})

# GET & POST API with GET,POST Parameter
@api_view(['GET','POST'])
def hello_world(request):
    if request.method == "GET":
        return Response({'msg:':'GET request Called'})
    if request.method == "POST":
        print(request.data)
        return Response({'msg':'POST request called','data':request.data})
