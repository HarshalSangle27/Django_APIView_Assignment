from django.urls import path
from .views import VendorListCreateAPIView, VendorDetailAPIView

urlpatterns = [
    # GET and POST for the entire list
    path('', VendorListCreateAPIView.as_view(), name='vendor-list-create'),
    
    # GET, PUT, PATCH, DELETE for a specific vendor ID
    # The <int:pk> captures the ID from the URL and passes it to your view
    path('<int:pk>/', VendorDetailAPIView.as_view(), name='vendor-detail'),
]