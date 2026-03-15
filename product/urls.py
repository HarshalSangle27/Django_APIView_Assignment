from django.urls import path
from .views import ProductListCreateAPIView, ProductDetailAPIView

urlpatterns = [
    # GET and POST for the entire list
    path('', ProductListCreateAPIView.as_view(), name='product-list-create'),
    
    # GET, PUT, PATCH, DELETE for a specific product ID
    # The <int:pk> captures the ID from the URL and passes it to your view
    path('<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
]