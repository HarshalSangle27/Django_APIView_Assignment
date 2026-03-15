from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CourseCertificationMapping
from .serializers import CourseCertificationMappingSerializer

class CourseCertificationMappingListCreateAPIView(APIView):
    @swagger_auto_schema(
        operation_description="List all mappings with optional filtering",
        manual_parameters=[
            openapi.Parameter('course_id', openapi.IN_QUERY, description="Filter by parent ID", type=openapi.TYPE_INTEGER),
        ],
        responses={200: CourseCertificationMappingSerializer(many=True)}
    )
    def get(self, request):
        mappings = CourseCertificationMapping.objects.all()
        
        # Filtering Requirement: query-param based filtering 
        course_id = request.query_params.get('course_id')
        if course_id:
            mappings = mappings.filter(course_id=course_id)

        serializer = CourseCertificationMappingSerializer(mappings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Create a new record",
        request_body=CourseCertificationMappingSerializer,
        responses={201: CourseCertificationMappingSerializer, 400: "Bad Request - Validation Errors"}
    )
    def post(self, request):
        serializer = CourseCertificationMappingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CourseCertificationMappingDetailAPIView(APIView):
    """
    API View to retrieve, update, or delete a single course-certification mapping by ID.
    """
    def get_object(self, pk):
        try:
            return CourseCertificationMapping.objects.get(pk=pk)
        except CourseCertificationMapping.DoesNotExist:
            return None

    @swagger_auto_schema(
        operation_description="Retrieve a specific record by ID",
        responses={200: CourseCertificationMappingSerializer, 404: "Not Found"}
    )
    def get(self, request, pk):
        mapping = self.get_object(pk)
        if not mapping:
            return Response({"error": "Mapping not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CourseCertificationMappingSerializer(mapping)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Update an entire record",
        request_body=CourseCertificationMappingSerializer,
        responses={200: CourseCertificationMappingSerializer, 400: "Bad Request", 404: "Not Found"}
    )
    def put(self, request, pk):
        mapping = self.get_object(pk)
        if not mapping:
            return Response({"error": "Mapping not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CourseCertificationMappingSerializer(mapping, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Partially update a record",
        request_body=CourseCertificationMappingSerializer,
        responses={200: CourseCertificationMappingSerializer, 400: "Bad Request", 404: "Not Found"}
    )
    def patch(self, request, pk):
        mapping = self.get_object(pk)
        if not mapping:
            return Response({"error": "Mapping not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CourseCertificationMappingSerializer(mapping, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete a record",
        responses={204: "No Content", 404: "Not Found"}
    )
    def delete(self, request, pk):
        mapping = self.get_object(pk)
        if not mapping:
            return Response({"error": "Mapping not found"}, status=status.HTTP_404_NOT_FOUND)
        
        mapping.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)