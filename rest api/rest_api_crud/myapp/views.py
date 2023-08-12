from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import student
from .serializer import studentSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.



# @api_view(['GET' , 'POST' , 'PUT' , 'PATCH' , 'DELETE'])
# def student_api(request,id=None):
#     if request.method == 'GET':
#         #id = pk 
#         if id is not None:
#             stu = student.objects.get(id = id)
#             serializer = studentSerializer(stu)
#             return Response(serializer.data)
#         stu = student.objects.all()
#         serializer = studentSerializer(stu , many = True)
#         return Response(serializer.data)
    
#     if request.method == 'POST':
#         serializer = studentSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg' : 'data created..'})
#         return Response(serializer.errors)

#     if request.method == 'PUT':
#         stu = student.objects.get(id = id)
#         serializer = studentSerializer(stu , data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg' : 'Data Updated..'})
#         return Response(serializer.errors)

#     if request.method == 'PATCH':
#         stu = student.objects.get(id = id)
#         serializer = studentSerializer(stu , data = request.data , partial = True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg' : 'Partially Data Updated..'})
#         return Response(serializer.errors)

#     if request.method == 'DELETE':
#         stu = student.objects.get(id = id)
#         stu.delete()
#         return Response({'msg' : 'Data Deleted..'})

#class based api view

class StudentApi(APIView):
    def get(self , request , id = None , format = None):
        if id is not None:
            stu = student.objects.get(id = id)
            serializer = studentSerializer(stu)
            return Response(serializer.data)
        stu = student.objects.all()
        serializer = studentSerializer(stu , many = True)
        return Response(serializer.data)

    def post(self , request , format = None):
        serializer = studentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : 'Data Created..'} , status = status.HTTP_201_CREATED)
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)

    def put(self , request , id , format = None):
        stu = student.objects.get(id = id)
        serializer = studentSerializer(stu , data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : 'Data Updated..'})
        return Response(serializer.errors)

    def patch(self , request , id , format = None):
        stu = student.objects.get(id = id)
        serializer = studentSerializer(stu , data = request.data , partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : 'Data Updated Partially..'})
        return Response(serializer.errors)

    def delete(self , request , id , format = None):
        stu = student.objects.get(id = id)
        stu.delete()
        return Response({'msg' : 'Data Deleted..'})

    authentication_classes = [JWTAuthentication]
    #permission_classes = [IsAuthenticated]


