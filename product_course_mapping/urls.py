from django.urls import path
from .views import ProductCourseMappingListCreateAPIView, ProductCourseMappingDetailAPIView

urlpatterns = [
    path('', ProductCourseMappingListCreateAPIView.as_view(), name='product-course-list-create'),
    path('<int:pk>/', ProductCourseMappingDetailAPIView.as_view(), name='product-course-detail'),
]