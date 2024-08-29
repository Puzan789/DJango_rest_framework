from django.shortcuts import render
from rest_framework.response import Response 
from .models import Student
from rest_framework import status 
from rest_framework import viewsets
from .serializers import StudentSerializer


class StudentViewSet(viewsets.ViewSet):
    def list(self,request):
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return Response(serializer.data)
    def retreive(self,request,pk=None):
        id=pk 
        if id is not None:
            stu=Student.objects.get(pk=id)
            serializer=StudentSerializer(stu)
            return Response(serializer.data)
    def create(self,request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Successfully created'})
    def update(self,request,pk=None):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
    def partial_update(self,request,pk):
        id=pk 
        stu=Student.objects.get(pk=id)
        serializer=StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self,request,pk=None):
        id=pk 
        stu=Student.objects.get(pk=id)
        stu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
              


        
