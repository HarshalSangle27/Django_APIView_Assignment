from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.shortcuts import render


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ProductCourseMapping
from .serializers import ProductCourseMappingSerializer

class ProductCourseMappingListCreateAPIView(APIView):
    @swagger_auto_schema(
        operation_description="List all mappings with optional filtering",
        manual_parameters=[
            openapi.Parameter('product_id', openapi.IN_QUERY, description="Filter by parent ID", type=openapi.TYPE_INTEGER),
        ],
        responses={200: ProductCourseMappingSerializer(many=True)}
    )
    def get(self, request):
        mappings = ProductCourseMapping.objects.all()
        
        
        product_id = request.query_params.get('product_id')
        if product_id:
            mappings = mappings.filter(product_id=product_id)

        serializer = ProductCourseMappingSerializer(mappings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Create a new record",
        request_body=ProductCourseMappingSerializer,
        responses={201: ProductCourseMappingSerializer, 400: "Bad Request - Validation Errors"}
    )
    def post(self, request):
        serializer = ProductCourseMappingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProductCourseMappingDetailAPIView(APIView):
    """
    API View to retrieve, update, or delete a single product-course mapping by ID.
    """
    def get_object(self, pk):
        try:
            return ProductCourseMapping.objects.get(pk=pk)
        except ProductCourseMapping.DoesNotExist:
            return None

    @swagger_auto_schema(
        operation_description="Retrieve a specific record by ID",
        responses={200: ProductCourseMappingSerializer, 404: "Not Found"}
    )
    def get(self, request, pk):
        mapping = self.get_object(pk)
        if not mapping:
            return Response({"error": "Mapping not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProductCourseMappingSerializer(mapping)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Update an entire record",
        request_body=ProductCourseMappingSerializer,
        responses={200: ProductCourseMappingSerializer, 400: "Bad Request", 404: "Not Found"}
    )
    def put(self, request, pk):
        mapping = self.get_object(pk)
        if not mapping:
            return Response({"error": "Mapping not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProductCourseMappingSerializer(mapping, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Partially update a record",
        request_body=ProductCourseMappingSerializer,
        responses={200: ProductCourseMappingSerializer, 400: "Bad Request", 404: "Not Found"}
    )
    def patch(self, request, pk):
        mapping = self.get_object(pk)
        if not mapping:
            return Response({"error": "Mapping not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProductCourseMappingSerializer(mapping, data=request.data, partial=True)
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