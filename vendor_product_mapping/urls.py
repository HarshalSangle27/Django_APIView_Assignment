from django.urls import path
from .views import VendorProductMappingListCreateAPIView, VendorProductMappingDetailAPIView

urlpatterns = [
    path('', VendorProductMappingListCreateAPIView.as_view(), name='vendor-product-list-create'),
    path('<int:pk>/', VendorProductMappingDetailAPIView.as_view(), name='vendor-product-detail'),
]