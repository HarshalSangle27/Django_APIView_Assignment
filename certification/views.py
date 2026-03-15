from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Certification
from .serializers import CertificationSerializer

class CertificationListCreateAPIView(APIView):
    """
    API View to list all vendors or create a new vendor.
    """
    @swagger_auto_schema(
        operation_description="List all records",
        responses={200: CertificationSerializer(many=True)}
    )
    def get(self, request):
        # Fetch all vendor objects from the database
        certifications = Certification.objects.all()
        # serialize them (many=True because it's a list)
        serializer = CertificationSerializer(certifications, many=True)
        # Return the data with a 200 OK status [cite: 153]
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Create a new record",
        request_body=CertificationSerializer,
        responses={201: CertificationSerializer, 400: "Bad Request - Validation Errors"}
    )
    def post(self, request):
        # Pass the incoming JSON payload to the serializer
        serializer = CertificationSerializer(data=request.data)
        # Validate the data (checks for required fields, unique 'code', etc.) [cite: 193]
        if serializer.is_valid():
            serializer.save()
            # Return the created data with a 201 Created status
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # If invalid, return the exact errors with a 400 Bad Request status
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CertificationDetailAPIView(APIView):
    """
    API View to retrieve, update, or delete a single vendor by ID.
    """
    # Helper method to handle "Does Not Exist" manually
    def get_object(self, pk):
        try:
            return Certification.objects.get(pk=pk)
        except Certification.DoesNotExist:
            return None

    @swagger_auto_schema(
        operation_description="Retrieve a specific record by ID",
        responses={200: CertificationSerializer, 404: "Not Found"}
    )
    def get(self, request, pk):
        certification = self.get_object(pk)
        if not certification:
            return Response({"error": "Certification not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CertificationSerializer(certification)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Update an entire record",
        request_body=CertificationSerializer,
        responses={200: CertificationSerializer, 400: "Bad Request", 404: "Not Found"}
    )
    def put(self, request, pk):
        # PUT requires all fields to be sent in the request
        certification = self.get_object(pk)
        if not certification:
            return Response({"error": "Certification not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CertificationSerializer(certification, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Partially update a record",
        request_body=CertificationSerializer,
        responses={200: CertificationSerializer, 400: "Bad Request", 404: "Not Found"}
    )
    def patch(self, request, pk):
        # PATCH allows partial updates (e.g., just changing the name)
        certification = self.get_object(pk)
        if not certification:
            return Response({"error": "Certification not found"}, status=status.HTTP_404_NOT_FOUND)
        
        # partial=True is the key difference from PUT
        serializer = CertificationSerializer(certification, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete a record",
        responses={204: "No Content", 404: "Not Found"}
    )
    def delete(self, request, pk):
        certification = self.get_object(pk)
        if not certification:
            return Response({"error": "Certification not found"}, status=status.HTTP_404_NOT_FOUND)
        
        certification.delete()
        # 204 No Content is the standard success status for deletion
        return Response(status=status.HTTP_204_NO_CONTENT)