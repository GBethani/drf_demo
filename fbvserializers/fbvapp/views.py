from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.
@api_view(['GET','POST'])
def student_list(request):
    if request.method == 'GET':
        students = Student.objects.all()
        get_serializer = StudentSerializer(students,many=True)
        return Response(get_serializer.data)
    elif request.method == 'POST':
        post_serializer = StudentSerializer(data=request.data)
        if post_serializer.is_valid():
            post_serializer.save()
            return Response(post_serializer.data,status=status.HTTP_201_CREATED)
        return Response(post_serializer.errors,status=status.HTTP_400_BAD_REQUEST) 

@api_view(['GET','PUT','DELETE'])
def student_detail(request,pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        get_serializer = StudentSerializer(student)
        return Response(get_serializer.data)
    elif request.method == 'POST':
        post_serializer = StudentSerializer(student,data=request.data)
        if post_serializer.is_valid():
            post_serializer.save()
            return Response(post_serializer.data)
        return Response(post_serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)