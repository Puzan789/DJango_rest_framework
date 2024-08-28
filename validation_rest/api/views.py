from django.shortcuts import render
from .models import Student
import io
from .serializers import StudentSerializer
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
# Create your views here.

@method_decorator(csrf_exempt,name='dispatch')
class StudentAPI(View):
    def get(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id=python_data.get('id',None)
        if id is not None :
            stu=Student.objects.get(id=id)
            serializer=StudentSerializer(stu)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type="application/json")
        else:
            stu=Student.objects.all()
            serializer=StudentSerializer(stu,many=True)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type="application/json")
    def post(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        serializer=StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            resp={"msg": "!!!!!Student created successfully!!!!!"}
            json_data=JSONRenderer().render(resp)
            return HttpResponse(json_data,content_type="application/json")
        else:
            json_data=JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data,content_type="application/json")
    def put(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id=python_data.get('id')
        stu=Student.objects.get(id=id)
        serializer=StudentSerializer(stu,data=python_data,partial=True)
        if serializer.is_valid():
            serializer.save()
            resp={"msg": "!!!!!Student updated successfully!!!!!"}
            json_data=JSONRenderer().render(resp)
            return HttpResponse(json_data,content_type="application/json")
        else:
            json_data=JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data,content_type="application/json")
        
    def delete(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id=python_data.get('id')
        stu=Student.objects.get(id=id)
        stu.delete()
        resp={"msg": "!!!!!Student Deleted successfully!!!!!"}
        json_data=JSONRenderer().render(resp)
        return HttpResponse(json_data,content_type="application/json")
        
  


    