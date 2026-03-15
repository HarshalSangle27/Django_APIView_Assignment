from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.shortcuts import render


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course
from .serializers import CourseSerializer

class CourseListCreateAPIView(APIView):
    """
    API View to list all vendors or create a new vendor.
    """
    @swagger_auto_schema(
        operation_description="List all records",
        responses={200: CourseSerializer(many=True)}
    )
    def get(self, request):
        
        courses = Course.objects.all()
        
        serializer = CourseSerializer(courses, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Create a new record",
        request_body=CourseSerializer,
        responses={201: CourseSerializer, 400: "Bad Request - Validation Errors"}
    )
    def post(self, request):
        
        serializer = CourseSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CourseDetailAPIView(APIView):
    """
    API View to retrieve, update, or delete a single vendor by ID.
    """
    
    def get_object(self, pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return None

    @swagger_auto_schema(
        operation_description="Retrieve a specific record by ID",
        responses={200: CourseSerializer, 404: "Not Found"}
    )
    def get(self, request, pk):
        course = self.get_object(pk)
        if not course:
            return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CourseSerializer(course)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Update an entire record",
        request_body=CourseSerializer,
        responses={200: CourseSerializer, 400: "Bad Request", 404: "Not Found"}
    )
    def put(self, request, pk):
        
        course = self.get_object(pk)
        if not course:
            return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    @swagger_auto_schema(
        operation_description="Partially update a record",
        request_body=CourseSerializer,
        responses={200: CourseSerializer, 400: "Bad Request", 404: "Not Found"}
    )
    def patch(self, request, pk):
        
        course = self.get_object(pk)
        if not course:
            return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)
        
        
        serializer = CourseSerializer(course, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete a record",
        responses={204: "No Content", 404: "Not Found"}
    )
    def delete(self, request, pk):
        course = self.get_object(pk)
        if not course:
            return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)
        
        course.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)