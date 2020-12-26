from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import generics,mixins
from rest_framework import viewsets
# Create your views here.
'''
class StudentList(APIView):

    def get(self,request):
        students = Student.objects.all()
        get_serializer = StudentSerializer(students,many=True)
        return Response(get_serializer.data)

    def post(self,request):
        post_serializer = StudentSerializer(data=request.data)
        if post_serializer.is_valid():
            post_serializer.save()
            return Response(post_serializer.data,status=status.HTTP_201_CREATED)
        return Response(post_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class StudentDetail(APIView):

    def get_object(self,pk):
        try:
            student = Student.objects.get(pk=pk)
            return student
        except Student.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        student = self.get_object(pk)
        get_serializer = StudentSerializer(student)
        return Response(get_serializer.data)

    def put(self,request,pk):
        student = self.get_object(pk)
        post_serializer = StudentSerializer(student,data=request.data)
        if post_serializer.is_valid():
            post_serializer.save()
            return Response(post_serializer.data)
        return Response(post_serializer.errors,status=status.HTTP_400_BAD_REQUEST) 

    def delete(self,request,pk):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''
'''
class StudentList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self,request):
        return self.list(request)

    def post(self,request):
        return self.create(request)

class StudentDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self,request,pk):
        return self.retrieve(request,pk)

    def put(self,request,pk):
        return self.update(request,pk)

    def delete(self,request,pk):
        return self.destroy(request,pk)
'''
'''
class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
'''

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer