from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,DestroyModelMixin,UpdateModelMixin

class Student_api(GenericAPIView,ListModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def get(self,request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
class Student_create(GenericAPIView,CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def post(self,request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class Student_retrieve(GenericAPIView,RetrieveModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def get(self,request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    


class Student_update(GenericAPIView,UpdateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def put(self,request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    


class Student_Delete(GenericAPIView,DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def delete(self,request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
