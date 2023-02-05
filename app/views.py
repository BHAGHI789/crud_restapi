from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.models import BookModel
from app.serializer import BookModelSerializer
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def list(request):
    obj=BookModel.objects.all()
    serializer=BookModelSerializer(obj,many=True)
    return Response(serializer.data)
@api_view(['POST'])
def Post_Book(request):
    obj=BookModel.objects.all()
    serializer=BookModelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['PUT'])
def update_book(request,pk):
    obj=BookModel.objects.get(id=pk)
    serializer=BookModelSerializer(instance=obj,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['DELETE'])
def delete_book(request,pk):
    obj=BookModel.objects.get(id=pk)
    obj.delete()
    return Response('item was delete')