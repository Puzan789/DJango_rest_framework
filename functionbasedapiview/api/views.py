from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

# @api_view()
# def hello(request):
#     return Response({"success": "hello"})

# @api_view(["GET"])
# def hello(request):
#     return Response({"success": "hello"})

# @api_view(["POST"])
# def hello(request):
#     if request.method == "POST":
#        return Response(request.data)

@api_view(["POST","GET"])
def hello(request):
    if request.method == "GET":
       return Response({"success": "This is get request"})
    if request.method == "POST":
       return Response({"data":request.data})
