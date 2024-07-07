from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import CrudEssay
from .serializer import CrudSerializer

# Create your views here.
@api_view(['GET'])
def test(request):
    try:
        
        essays = CrudEssay.objects.all()
        serializer = CrudSerializer(essays, many=True)
        return Response(serializer.data)
    except CrudEssay.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        # Log the exception (optional: use a logging framework)
        print(f"An error occurred: {e}")
        return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def getById(request, id):
    try:
        essay = CrudEssay.objects.get(pk=id)
        serializer = CrudSerializer(essay)
        return Response(serializer.data)
    except CrudEssay.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

@api_view(['POST'])
def create(request):
    serializer = CrudSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update(request, id):
    product= get_object_or_404(CrudEssay, pk=id)
    serializer= CrudSerializer(product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['DELETE'])
def delete(request, id ):
    try:
        essay = get_object_or_404(CrudEssay, pk=id)
        essay.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except CrudEssay.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)



