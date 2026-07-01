from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.


@api_view(['GET', 'POST'])
def publication_list(request):
    if request.method == 'GET':
        return Response("ok")
    if request.method == 'POST':
        return Response("ok")


@api_view(['GET', 'PATCH', 'DELETE'])
def publication_details(request, pk):
    if request.method == 'GET':
        return Response(f"ok {pk}")
    if request.method == 'PATCH':
        return Response(f"ok {pk}")
    if request.method == 'DELETE':
        return Response(f"ok {pk}")
    
