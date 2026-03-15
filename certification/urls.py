from django.urls import path
from .views import CertificationListCreateAPIView, CertificationDetailAPIView

urlpatterns = [
    # GET and POST for the entire list
    path('', CertificationListCreateAPIView.as_view(), name='certification-list-create'),
    
    # GET, PUT, PATCH, DELETE for a specific certification ID
    # The <int:pk> captures the ID from the URL and passes it to your view
    path('<int:pk>/', CertificationDetailAPIView.as_view(), name='certification-detail'),
]