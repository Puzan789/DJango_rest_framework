from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
# Model Object 

def student_detail(request,pk):
    stu=Student.objects.get(id=pk)
    # print(stu)
    serializer = StudentSerializer(stu)
    # print(serializer)
    # print(serializer.data)
    # json_data=JSONRenderer().render(serializer.data)
    # # print(json_data)  # json string ko bhanney  # 500 error 404 not found error 400 bad request error 200 ok response  # 500 error is server error 404 not found error is client error 400 bad request error is client error
    # return HttpResponse(json_data,content_type="application/json") # json type ko bhanney
    return JsonResponse(serializer.data)

# query sets
def student_list(request):
    stu=Student.objects.all()
    # print(stu)
    serializer = StudentSerializer(stu,many=True)
    # # print(serializer)
    # # print(serializer.data)
    # json_data=JSONRenderer().render(serializer.data)
    # # print(json_data)  # json string ko bhanney  # 500 error 404 not found error 400 bad request error 200 ok response  # 500 error is server error 404 not found error is client error 400 bad request error is client error
    # return HttpResponse(json_data,content_type="application/json") # json type ko bhanney
    return JsonResponse(serializer.data,safe=False)


