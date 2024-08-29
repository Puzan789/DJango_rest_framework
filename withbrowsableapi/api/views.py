from django.shortcuts import render
from .models import Student
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer
from rest_framework import status


@api_view(['GET','POST','PUT','DELETE','PATCH'])
def student_api(request,pk=None):
    if request.method =="GET":
        id=pk
        if id is not None :
            stu=Student.objects.get(pk=id)
            serializer=StudentSerializer(stu)
            return Response(serializer.data)
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    if request.method == "POST":
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Created data succesfully"})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            
    if request.method == "PUT":
        id=pk
        stu=Student.objects.get(pk=id)
        serializer=StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Updated data successfully"})
    if request.method == "PATCH":
        id=pk
        stu=Student.objects.get(pk=id)
        serializer=StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Updated data successfully"})
        
    if request.method == "DELETE":
        id=pk
        stu=Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':"Deleted data successfully"})