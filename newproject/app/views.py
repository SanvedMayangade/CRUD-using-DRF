from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from django.http  import JsonResponse
from .serializer import *



# Create your views here.
@api_view(['GET'])
def get(request):
    obj = Students.objects.all()
    ser = studentserializers(obj, many=True)
    
    return Response({
    'data': ser.data
        } )


@api_view(['POST'])
def post_data(request):
    try:
        data = request.data
        serializer = studentserializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    except Exception as e:
        print(e)

@api_view(['POST'])
def update_data(request,pk):
    try:
        obj=Students.objects.get(id=pk)
        ser = studentserializers(instance=obj,data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
    except Exception as e:
        print(e)

@api_view(["DELETE"])
def delete_data(request,pk):
    obj=Students.objects.get(id=pk)
    obj.delete()
    return Response({"data":"data deleted successfully"})
